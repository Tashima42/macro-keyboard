import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keyboard = Keyboard(usb_hid.devices)

# OPTIONS
SLEEP_TIME = 0.3
MOD_KEY = Keycode.WINDOWS

# LAYOUT
"""
+--------------------+------------------------+--------------+
| BTN0               | BTN1                   | BTN2         |
| MOD + 1            | MOD + 4                | MOD + 9      |
| WORSKPACE 1        | WORKSPACE 4            | WORKSPACE 9  |
+--------------------+------------------------+--------------+
| BTN3               | BTN4                   | BTN5         |
| MOD + 10           | MOD + SHIFT + a        | MOD + SHIFT + a        |
| MOVE TO SCRATCHPAD | MOVE OUT OF SCRATCHPAD | WORKSPACE 10 |
+--------------------+------------------------+--------------+
| BTN6               | BTN7                   | BTN8         |
| MOD + SHIFT + I    | MOD + SHIFT + O        |              |
| KEYBOARD LAYOUT BR | KEYBOARD LAYOUT US     |              |
+--------------------+------------------------+--------------+
"""

# Declaring buttons
BTNS = [
        # CHANGE TO WORKSPACE ONE
        {
            "io": digitalio.DigitalInOut(board.GP7),
            "keys": [MOD_KEY, Keycode.ONE]
        },
        # CHANGE TO WORKSPACE FOUR
        {
            "io": digitalio.DigitalInOut(board.GP8),
            "keys": [MOD_KEY, Keycode.FOUR]
        },
        # CHANGE TO WORKSPACE NINE
        {
            "io": digitalio.DigitalInOut(board.GP9),
            "keys": [MOD_KEY, Keycode.NINE]
        },
        # WORKSPACE 10
        {
            "io": digitalio.DigitalInOut(board.GP10),
            "keys": [MOD_KEY, Keycode.ZERO]
        },
        # KEYBOARD LAYOUT BR
        {
            "io": digitalio.DigitalInOut(board.GP11),
            "keys": [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.I]
        },
        # KEYBOARD LAYOUT US
        {
            "io": digitalio.DigitalInOut(board.GP12),
            "keys": [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.O]
        },
        # MOVE WINDOW TO SCRATCHPAD
        {
            "io": digitalio.DigitalInOut(board.GP13),
            "keys": [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.A]
        },
        # MOVE WINDOW OUT OF SCRATCHPAD
        {
            "io": digitalio.DigitalInOut(board.GP14),
            "keys": [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.S]
        },
        # TOGGLE FLOATING
        {
            "io": digitalio.DigitalInOut(board.GP15),
            "keys": [MOD_KEY, Keycode.LEFT_SHIFT, Keycode.SPACE]
        }
]

def pressKeys(keys): 
    for key in keys:
        keyboard.press(key)
    time.sleep(SLEEP_TIME)
    for key in keys:
        keyboard.release(key)

for BTN in BTNS:
    BTN["io"].direction = digitalio.Direction.INPUT
    BTN["io"].pull = digitalio.Pull.DOWN

while True:
	# Check if button is pressed and if it is, to press the Macros
    for BTN in BTNS:
        if BTN["io"].value:
            pressKeys(BTN["keys"])
