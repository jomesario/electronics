import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    boton_estado=GPIO.input(21)
    if boton_estado == False:
        GPIO.output(18,True)
    else:
        GPIO.output(18, False)
