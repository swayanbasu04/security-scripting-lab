## Python Keylogger Project
A lightweight, class-based keylogger written in Python.

## Prerequisites
This script requires the keyboard library to function. You can install it via pip:
```bash
pip install keyboard
```
*Note: On Linux systems, this script must be run with sudo privileges to successfully hook into the keyboard events.*

## How to Run
 1. Ensure you have the required dependencies installed.
 2. Run the script using Python 3:
   ```bash
   sudo python3 keylog.py
   ```
 3. To stop the logger and save any remaining data in the buffer, press the **ESC** key.

## Project Structure
 * keylog.py: The main execution script.
 * system_keylog.txt: The output file where keystrokes are recorded.

## Features
 * **Class-Based Architecture:** Uses an object-oriented approach for better code modularity.
 * **Buffered Logging:** Instead of writing to the disk on every single key press (which causes I/O bottlenecks), the script buffers keystrokes and writes them in batches.
 * **Dynamic Formatting:** Automatically detects and formats special keys (like [ENTER], [BACKSPACE], [SHIFT]) for better log readability.
 * **Timestamping:** Every batch of logged data is timestamped for easy auditing.

## Ethical Disclaimer
- Use this tool only the systems you own or have proper permission


                                  ----------------_______----------------
  
