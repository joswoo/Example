import RPi.GPIO as GPIO
import time

led_red = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_red, GPIO.OUT)

try:
    while(True):
        GPIO.output(led_red, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_red, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
