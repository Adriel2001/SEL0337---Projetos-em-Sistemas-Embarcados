import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "Adriel 11914299"

print("Aproxime a TAG do leitor...")
leitor.write(texto)

print("Concluido!")