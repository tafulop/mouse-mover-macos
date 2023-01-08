#!/usr/bin/python3

import macmouse
from pynput import keyboard

def move_to_position_1():
    print("Moving to position 1.")
    macmouse.move(x=100, y=100)

def move_to_position_2():
    print("Moving to position 2.")
    macmouse.move(x=500, y=500)

with keyboard.GlobalHotKeys(
    {
     "<ctrl>+<alt>+h": move_to_position_1,
     "<ctrl>+<alt>+j": move_to_position_2
    }
) as h:
    h.join()
