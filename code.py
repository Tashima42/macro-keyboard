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
| BTN1               | BTN2                   | BTN3         |
| MOD + 1            | MOD + 4                | MOD + 9      |
| WORSKPACE 1        | WORKSPACE 4            | WORKSPACE 9  |
+--------------------+------------------------+--------------+
| BTN4               | BTN5                   | BTN6         |
| MOD + SHIFT + A    | MOD + SHIFT + S        | MOD + 0      |
| MOVE TO SCRATCHPAD | MOVE OUT OF SCRATCHPAD | WORKSPACE 10 |
+--------------------+------------------------+--------------+
| BTN7               | BTN8                   | BTN9         |
| MOD + SHIFT + I    | MOD + SHIFT + O        |              |
| KEYBOARD LAYOUT BR | KEYBOARD LAYOUT US     |              |
+--------------------+------------------------+--------------+
"""

# Declaring buttons
BTN1_PIN = board.GP7
BTN2_PIN = board.GP8
BTN3_PIN = board.GP9
BTN4_PIN = board.GP10
BTN5_PIN = board.GP11
BTN6_PIN = board.GP12
BTN7_PIN = board.GP13
BTN8_PIN = board.GP14
BTN9_PIN = board.GP15

# Initializing Buttons
BTN1 = digitalio.DigitalInOut(BTN1_PIN)
BTN1.direction = digitalio.Direction.INPUT
BTN1.pull = digitalio.Pull.DOWN
BTN1_BOOL = False

BTN2 = digitalio.DigitalInOut(BTN2_PIN)
BTN2.direction = digitalio.Direction.INPUT
BTN2.pull = digitalio.Pull.DOWN
BTN2_BOOL = False

BTN3 = digitalio.DigitalInOut(BTN3_PIN)
BTN3.direction = digitalio.Direction.INPUT
BTN3.pull = digitalio.Pull.DOWN
BTN3_BOOL = False

BTN4 = digitalio.DigitalInOut(BTN4_PIN)
BTN4.direction = digitalio.Direction.INPUT
BTN4.pull = digitalio.Pull.DOWN
BTN4_BOOL = False

BTN5 = digitalio.DigitalInOut(BTN5_PIN)
BTN5.direction = digitalio.Direction.INPUT
BTN5.pull = digitalio.Pull.DOWN
BTN5_BOOL = False

BTN6 = digitalio.DigitalInOut(BTN6_PIN)
BTN6.direction = digitalio.Direction.INPUT
BTN6.pull = digitalio.Pull.DOWN
BTN6_BOOL = False

BTN7 = digitalio.DigitalInOut(BTN7_PIN)
BTN7.direction = digitalio.Direction.INPUT
BTN7.pull = digitalio.Pull.DOWN
BTN7_BOOL = False

BTN8 = digitalio.DigitalInOut(BTN8_PIN)
BTN8.direction = digitalio.Direction.INPUT
BTN8.pull = digitalio.Pull.DOWN
BTN8_BOOL = False

BTN9 = digitalio.DigitalInOut(BTN9_PIN)
BTN9.direction = digitalio.Direction.INPUT
BTN9.pull = digitalio.Pull.DOWN
BTN9_BOOL = False

while True:
	# Check if button is pressed and if it is, to press the Macros

    # CHANGE TO WORKSPACE ONE
    if BTN1.value:  
        print("BTN 1")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.ONE)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.ONE)
        BTN1_BOOL = not BTN1_BOOL
    # CHANGE TO WORKSPACE FOUR
    if BTN2.value:  
        print("BTN 2")
        keyboard.press(MOD_KEY)
        time.sleep(0.1)
        keyboard.press(Keycode.FOUR)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.FOUR)
        BTN2_BOOL = not BTN2_BOOL
    # CHANGE TO WORKSPACE NINE
    if BTN3.value:  
        print("BTN 3")
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.NINE)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.NINE)
        BTN3_BOOL = not BTN3_BOOL
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
        BTN4_BOOL = not BTN4_BOOL
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
        BTN5_BOOL = not BTN5_BOOL
    # 
    if BTN6.value:  
        print("BTN 6")
        """
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.I)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.I)
        BTN7_BOOL = not BTN7_BOOL
        """
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
        BTN7_BOOL = not BTN7_BOOL
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
        BTN8_BOOL = not BTN8_BOOL
    # 
    if BTN9.value:  
        print("BTN 9")
        """
        keyboard.press(MOD_KEY)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.I)
        time.sleep(SLEEP_TIME)
        keyboard.release(MOD_KEY)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.I)
        BTN7_BOOL = not BTN7_BOOL
        """
