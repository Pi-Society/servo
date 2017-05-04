
import RPi.GPIO as GPIO
from time import sleep

FAR_LEFT=12
FAR_RIGHT=2
MIDDLE=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)

pwm.start(5)

sleep(2)

pwm.ChangeDutyCycle(FAR_LEFT)

sleep(2)

pwm.ChangeDutyCycle(FAR_RIGHT)

sleep(2)

pwm.stop()
GPIO.cleanup()
