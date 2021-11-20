import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keyboard = Keyboard(usb_hid.devices)

# OPTIONS
SLEEP_TIME = 0.15
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
        [ board.GP7 ],
        [ board.GP8 ],
        [ board.GP9 ],
        [ board.GP10 ],
        [ board.GP11 ],
        [ board.GP12 ],
        [ board.GP13 ],
        [ board.GP14 ],
        [ board.GP15 ] 
]

for BTN in BTNS:
    BTN.append(digitalio.DigitalInOut(BTN[0]))
    BTN[1].direction = digitalio.Direction.INPUT
    BTN[1].pull = digitalio.Pull.DOWN

while True:
	# Check if button is pressed and if it is, to press the Macros

    # CHANGE TO WORKSPACE ONE
    if BTNS[0][1].value:  
        print("BTN 0")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.ONE)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.ONE)
"""
    # CHANGE TO WORKSPACE FOUR
    if BTN2.value:  
        print("BTN 2")
        keyboard.press(MOD_KEY)
        time.sleep(0.1)
        keyboard.press(Keycode.FOUR)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.FOUR)
    # CHANGE TO WORKSPACE NINE
    if BTN3.value:  
        print("BTN 3")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.NINE)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.NINE)
    # MOVE WINDOW TO SCRATCHPAD
    if BTN4.value:  
        print("BTN 4")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.A)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.A)
    # MOVE WINDOW OUT OF SCRATCHPAD
    if BTN5.value:  
        print("BTN 5")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.S)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.S)
    # 
    if BTN6.value:  
        print("BTN 6")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.I)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.I)
    # KEYBOARD LAYOUT BR
    if BTN7.value:  
        print("BTN 7")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.I)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.I)
    # KEYBOARD LAYOUT US
    if BTN8.value:  
        print("BTN 8")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.O)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.O)
    # 
    if BTN9.value:  
        print("BTN 9")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.I)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.I)
"""
