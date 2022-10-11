#verificar acentos

r1 = "Bela Vista, 25 de março de 1966\n\n\nInesquecível Silvestre \n\n\nRecebi dia 23 sua carta do dia 13. Já estava preocupada sem notícias sua, pensei até que já estivesse me esquecido. Mas fiquei bastante contente com sua cartinha que por umas horas desapareceu está tristeza infinita que consome meus dias. Para mim, aqui sem você tudo é triste, por mais que eu procure fazer qualquer serviço para me distrair, cuidar das plantas, dos coelhos, sinto ainda mais saudades sua. Já quero que esteja ao meu lado. Já estava mesmo em falta com você, mas sei que você tem um bom coração, abuso de sua bondade como sei que vai me perdoar."

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
 	   p.text(r1)
 	   time.sleep(30) # Aguarda por 30 segundo

	else:
	    GPIO.output("P9_42", GPIO.LOW)

	GPIO.cleanup()
