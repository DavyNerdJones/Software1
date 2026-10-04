#Script:
import string
import time
from pynput.keyboard import Controller, Key, Listener

keyboard = Controller()
running = False

def auto_type():
    print("Auto-typer started! Press 'F8' to stop.")
    letters = string.ascii_lowercase  # 'a' through 'z'
    
    delay = 1.0 / 60.0 

    while running:
        for char in letters:
            if not running:
                break
            keyboard.press(char)
            keyboard.release(char)
        
        time.sleep(delay)

def on_press(key):
    global running
    
    if key == Key.f8:
        running = not running
        if running:
            import threading
            threading.Thread(target=auto_type, daemon=True).start()
        else:
            print("Auto-typer paused.")

def main():
    print("=== Dota 2 Auto-Typer Macro ===")
    print("Press [F8] to START / PAUSE the script.")
    print("Press [Ctrl + C] in this terminal to EXIT.")
    
    with Listener(on_press=on_press) as listener:
        listener.join()

if _name_ == "__main__":
    main()