#!/usr/bin/python3

import macmouse
import time

while True:
    x, y = macmouse.get_position()
    print("x: ", x, "y: ", y)
    time.sleep(1)