import  RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class Servo:
    def __init__(self):
        self.run()
    def run(self):
        pwm = GPIO.PWM(17,50)
        pwm.start(0)
            
        pwm.ChangeDutyCycle(1.5)
        sleep(15)


        pwm.ChangeDutyCycle(17.50)
        pwm.stop()

