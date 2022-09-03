import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
punto_espera=0.1*2
guion_espera=0.3*2
caracter_espacio=0.3*2
espera_default=0.1*3
letra_espera=.2*2

frase=input("Por favor introduce la frase a traducir\n")
diccionario = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : ".-.."
}



def prender_punto():
    GPIO.output(18,True)
    time.sleep(punto_espera)
    GPIO.output(18, False)
    time.sleep(espera_default)

def prender_guion():
    GPIO.output(18,True)
    time.sleep(guion_espera)
    GPIO.output(18, False)
    time.sleep(espera_default)

def prender_letra(letra):
    letra_morse = diccionario[letra]
    for c in letra_morse:
        if(c=="."):
            prender_punto()
        else:
            prender_guion()
    time.sleep(letra_espera)

for c in frase.lower():
    if (c == " "):
        time.sleep(caracter_espacio)
    else:
        prender_letra(c)

