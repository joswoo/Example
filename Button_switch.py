import RPi.GPIO as GPIO

LED = 12
Button = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(Button,GPIO.IN)
BUTTON_state = 0

try:
    while True:       
        if GPIO.input(Button)==1:
            BUTTON_state = not BUTTON_state
            GPIO.output(LED,BUTTON_state)
        

except KeyboardInterrupt:
    GPIO.cleanup()
