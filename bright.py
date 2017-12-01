import RPi.GPIO as GPIO
import time
 
led_red = 12
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_red, GPIO.OUT)
 
pwm_led = GPIO.PWM(led_red,500)
pwm_led.start(100)

try:
    while(True):
        duty_s = input("Enter Brightness (0 to 100):")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    GPIO.cleanup()
