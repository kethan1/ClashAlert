import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pinlist = [17, 27, 22, 23]
GPIO.setup(pinlist, GPIO.OUT)
GPIO.output([17, 27], GPIO.LOW)
GPIO.output([22, 23], GPIO.LOW)