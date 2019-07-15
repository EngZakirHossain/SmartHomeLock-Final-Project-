import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
pwm=GPIO.PWM(12, 50)
pwm.start(0)
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)
	pwm.stop()
	SetAngle(90)
GPIO.cleanup()
GPIO.setwarnings(False)

