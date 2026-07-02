from scapy.all import IP, AsyncSniffer, Raw, conf, hexdump, raw
import logging
import os
import signal
import sys
import threading
import termios
import tty
import select

if os.geteuid() != 0:
    print("[!] Error: This script must be run as root (sudo)")
    print("[*] Try: sudo python3 packet_analyzer.py")
    exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def describe_packet(packet):
    print(packet.summary())
    print(packet.show(dump=True))

    try:
        packet_bytes = raw(packet)
        if packet_bytes:
            print("Hexdump:")
            hexdump(packet_bytes)
    except Exception as exc:
        logging.exception("Failed to render packet bytes: %s", exc)


def wait_for_ctrl_x(stop_event, sniffer):
    if not sys.stdin.isatty():
        return

    fd = sys.stdin.fileno()
    original_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        print("[+] Press Ctrl+X to stop capture.")

        while not stop_event.is_set():
            ready, _, _ = select.select([sys.stdin], [], [], 0.2)
            if not ready:
                continue

            char = sys.stdin.read(1)
            if char == "\x18":
                print("\n[!] Capture stopped by user (Ctrl+X).")
                stop_event.set()
                sniffer.stop()
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)

def packet_callback(packet):
    try:
        if IP not in packet:
            return

        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        protocol_name = {
            1: "ICMP",
            6: "TCP",
            17: "UDP",
        }.get(protocol, f"Other ({protocol})")

        logging.info("New Packet: %s -> %s | Protocol: %s", src_ip, dst_ip, protocol_name)
        print(f"source IP: {src_ip} -> destination IP: {dst_ip} | Protocol: {protocol_name}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            if payload:
                print(f"Payload bytes: {payload[:100]!r}")

        describe_packet(packet)
        print("-" * 50)
    except Exception as exc:
        logging.exception("Error while handling packet: %s", exc)
      
print(f"Script Name: {__file__} ")

default_iface = conf.iface

def main():
    logging.info("Starting packet capture on %s", default_iface)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    stop_event = threading.Event()
    sniffer = AsyncSniffer(iface=default_iface, filter="ip", prn=packet_callback, store=False)

    try:
        sniffer.start()
        keyboard_thread = threading.Thread(target=wait_for_ctrl_x, args=(stop_event, sniffer), daemon=True)
        keyboard_thread.start()

        while sniffer.running and not stop_event.is_set():
            stop_event.wait(timeout=0.2)

    except Exception as exc:
        logging.exception("Packet capture failed: %s", exc)
    finally:
        if sniffer.running:
            sniffer.stop()


if __name__ == "__main__":
    main()
