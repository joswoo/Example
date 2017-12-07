import RPi.GPIO as GPIO
import time
import random
 
led_red = 12
led_yellow = 16
led_green = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

led_random = [led_red, led_yellow, led_green]

try:
    while(True):
        LED = random.choice(led_random)
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
