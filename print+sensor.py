import Adafruit_BBIO.GPIO as GPIO
from escpos import *

p = printer.Usb(0x28e9, 0x0289)


GPIO.setup("P9_42", GPIO.OUT)
GPIO.setup("P9_41", GPIO.IN)


while 1:


	if GPIO.input("P9_41"):
 	   GPIO.output("P9_42", GPIO.HIGH)
 	   p.text("Taina <3\n")

	else:
	    GPIO.output("P9_42", GPIO.LOW)

	GPIO.cleanup()
