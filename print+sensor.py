
import Adafruit_BBIO.GPIO as GPIO
from escpos import *
import time

#cria a impressora
p = printer.Usb(0x28e9, 0x0289)

#setup dos pinos
GPIO.setup("P9_42", GPIO.OUT)
GPIO.setup("P9_41", GPIO.IN)

#Se identificou botão imprime e espera
print("Programa Iniciado")
while 1:


	if GPIO.input("P9_41"):
 	   GPIO.output("P9_42", GPIO.HIGH)
 	   p.text("Teste\n")
 	   time.sleep(30) # Aguarda por 30 segundo

	else:
	    GPIO.output("P9_42", GPIO.LOW)

	GPIO.cleanup()
