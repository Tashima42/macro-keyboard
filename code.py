import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keyboard = Keyboard(usb_hid.devices)

# OPTIONS
SLEEP_TIME = 0.5
MOD_KEY = Keycode.WINDOWS

# LAYOUT
"""
+--------------------+------------------------+--------------+
| BTN0               | BTN1                   | BTN2         |
| MOD + 1            | MOD + 4                | MOD + 9      |
| WORSKPACE 1        | WORKSPACE 4            | WORKSPACE 9  |
+--------------------+------------------------+--------------+
| BTN3               | BTN4                   | BTN5         |
| MOD + SHIFT + A    | MOD + SHIFT + S        | MOD + 0      |
| MOVE TO SCRATCHPAD | MOVE OUT OF SCRATCHPAD | WORKSPACE 10 |
+--------------------+------------------------+--------------+
| BTN6               | BTN7                   | BTN8         |
| MOD + SHIFT + I    | MOD + SHIFT + O        |              |
| KEYBOARD LAYOUT BR | KEYBOARD LAYOUT US     |              |
+--------------------+------------------------+--------------+
"""

# Declaring buttons
BTNS = [
        digitalio.DigitalInOut(board.GP7), 
        digitalio.DigitalInOut(board.GP8),
        digitalio.DigitalInOut(board.GP9),
        digitalio.DigitalInOut(board.GP10),
        digitalio.DigitalInOut(board.GP11),
        digitalio.DigitalInOut(board.GP12),
        digitalio.DigitalInOut(board.GP13),
        digitalio.DigitalInOut(board.GP14),
        digitalio.DigitalInOut(board.GP15) 
]

KEYS = [
    [MOD_KEY, Keycode.ONE],
]

for BTN in BTNS:
    BTN.direction = digitalio.Direction.INPUT
    BTN.pull = digitalio.Pull.DOWN

def pressKeys(keys): 
    for key in keys:
        keyboard.press(key)
    time.sleep(SLEEP_TIME)
    for key in keys:
        keyboard.release(key)

while True:
	# Check if button is pressed and if it is, to press the Macros

    # CHANGE TO WORKSPACE ONE
    if BTNS[0].value:  
        print("BTN 0")
        pressKeys([MOD_KEY, Keycode.ONE])
    # CHANGE TO WORKSPACE FOUR
    if BTNS[1].value:  
        print("BTN 1")
        pressKeys([MOD_KEY, Keycode.FOUR])
    # CHANGE TO WORKSPACE NINE
    if BTNS[2].value:  
        print("BTN 2")
        pressKeys([MOD_KEY, Keycode.NINE])
    # MOVE WINDOW TO SCRATCHPAD
    if BTNS[3].value:  
        print("BTN 3")
        pressKeys([MOD_KEY, Keycode.LEFT_SHIFT, Keycode.A])
    # MOVE WINDOW OUT OF SCRATCHPAD
    if BTNS[4].value:  
        print("BTN 4")
        pressKeys([MOD_KEY, Keycode.LEFT_SHIFT, Keycode.S])
    # WORKSPACE 10
    if BTNS[5].value:  
        print("BTN 5")
        pressKeys([MOD_KEY, Keycode.ZERO])
    # KEYBOARD LAYOUT BR
    if BTNS[6].value:  
        print("BTN 6")
        pressKeys([MOD_KEY, Keycode.LEFT_SHIFT, Keycode.I])
    # KEYBOARD LAYOUT US
    if BTNS[7].value:  
        print("BTN 7")
        pressKeys([MOD_KEY, Keycode.LEFT_SHIFT, Keycode.O])
    # WORKSPACE 2
    if BTNS[8].value:  
        print("BTN 8")
        pressKeys([MOD_KEY, Keycode.TWO])
