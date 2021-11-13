import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinlist = [17, 27, 22, 23]
GPIO.setup(pinlist, GPIO.OUT)

GPIO.output([17, 22], GPIO.HIGH)
time.sleep(5)
GPIO.output([17, 22], GPIO.LOW)
