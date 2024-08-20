import RPi.GPIO as GPIO

class Vibration:
    def __init__(self,PIN_VIBRATION=18):
        self.PIN_VIBRATION = PIN_VIBRATION
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_VIBRATION, GPIO.OUT)

    def motor_on(self):
        GPIO.output(self.PIN_VIBRATION, GPIO.HIGH)

    def motor_off(self):
        GPIO.output(self.PIN_VIBRATION, GPIO.LOW)
