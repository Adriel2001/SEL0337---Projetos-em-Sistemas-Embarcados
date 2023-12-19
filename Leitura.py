import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#Inicializando com os pinos baixos
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

leitor = SimpleMFRC522()

while True:

    id, texto = leitor.read()

    if((texto.strip() == "Adriel 11914299") and (id == 771459753502)):
        print("Tag reconhecida, Acesso liberado!")
        #LED Verde acende
        GPIO.output(17, GPIO.HIGH)
    else:
        print("Acesso Negado!")
        #LED Vermelho acende
        GPIO.output(22, GPIO.HIGH)

    sleep(3)

    #Reseta os pinos para LOW novamente
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)