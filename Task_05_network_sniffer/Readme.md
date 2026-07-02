## Network Packet Analyzer
A python-based network sniffer built using the [scapy](https://scapy.net/) library. 

## Requirements
- Linux
- Python3
- Scapy (`pip install scapy`)

## Run 
The script must be run with root or sudo privileges:
```bash
 sudo python3 packet-analyzer.py
```

## Controls
- Press ctrl+x to stop the capture and exit the program

## What you'll see
- source and destination ip address
- protocol names like TCP, UDP. ICMP, or other
- `raw(packet)` and `hexdump()` out put when its available
- `packet.summary()` output
- `packet.show(dump=true)` output

## Ethical Disclaimer
- Use this tool only on networks and systems you own or are authorized to inspect
- Do not capture traffic without permission

                                  ----------------_______----------------
