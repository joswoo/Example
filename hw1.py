import RPi.GPIO as GPIO
import time
 
led_red = 12
led_yellow = 16
led_green = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

try:
    while(True):
        GPIO.output(led_red,GPIO.HIGH)
        GPIO.output(led_yellow,GPIO.HIGH)
        GPIO.output(led_green,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_red,GPIO.LOW)
        GPIO.output(led_yellow,GPIO.LOW)
        GPIO.output(led_green,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
     GPIO.cleanup()
