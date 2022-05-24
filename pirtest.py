# from machine import Pin
import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

pir = digitalio.DigitalInOut(board.GP16)
hpir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.DOWN

state = "waiting"

time.sleep(3)
while True:
   if pir.value == True and state == "waiting":
       state = "moving"
       print(state)
       kbd.send( Keycode.H)
   elif pir.value == False and state == "moving":
       state = "waiting"
       print(state)
       kbd.send( Keycode.R)
time.sleep(0.2)