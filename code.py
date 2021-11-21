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
BTNS = {
        # CHANGE TO WORKSPACE ONE
        digitalio.DigitalInOut(board.GP7): [MOD_KEY, Keycode.ONE],

        # CHANGE TO WORKSPACE FOUR
        digitalio.DigitalInOut(board.GP8): [MOD_KEY, Keycode.FOUR],

        # CHANGE TO WORKSPACE NINE
        digitalio.DigitalInOut(board.GP9): [MOD_KEY, Keycode.NINE],

        # MOVE WINDOW TO SCRATCHPAD
        digitalio.DigitalInOut(board.GP10): [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.A],

        # MOVE WINDOW OUT OF SCRATCHPAD
        digitalio.DigitalInOut(board.GP11): [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.S],

        # WORKSPACE 10
        digitalio.DigitalInOut(board.GP12): [MOD_KEY, Keycode.ZERO],

        # KEYBOARD LAYOUT BR
        digitalio.DigitalInOut(board.GP13): [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.I],

        # KEYBOARD LAYOUT US
        digitalio.DigitalInOut(board.GP14): [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.O],

        # WORKSPACE 2
        digitalio.DigitalInOut(board.GP15): [MOD_KEY, Keycode.TWO]
}

for BTN in BTNS.keys():
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

    for bnt in BTNS.keys():
        if bnt.value:
            pressKeys(BTNS[bnt])
