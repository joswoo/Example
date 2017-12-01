import RPi.GPIO as GPIO

LED = 12
Button = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(Button,GPIO.IN)

try:
    while True:       
        if GPIO.input(Button)==0:
            GPIO.output(LED,GPIO.HIGH)
        else:
            GPIO.output(12,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
