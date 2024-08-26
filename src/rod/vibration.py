import RPi.GPIO as GPIO

class Vibration:
    def __init__(self, PIN_IN1=23, PIN_IN2=24):
        self.PIN_IN1 = PIN_IN1  
        self.PIN_IN2 = PIN_IN2  
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_IN1, GPIO.OUT)
        GPIO.setup(self.PIN_IN2, GPIO.OUT)
        
        GPIO.output(self.PIN_IN1, GPIO.LOW)
        GPIO.output(self.PIN_IN2, GPIO.LOW)

    def motor_on(self):
        GPIO.output(self.PIN_IN1, GPIO.HIGH)
        GPIO.output(self.PIN_IN2, GPIO.LOW) 
        print("モータをオンにします")

    def motor_off(self):
        GPIO.output(self.PIN_IN1, GPIO.LOW)
        GPIO.output(self.PIN_IN2, GPIO.LOW)  
        print("モータをオフにします")

    
