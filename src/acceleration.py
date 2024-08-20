import time
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import pygame
import vibration as vib

# センサーとGPIOの設定
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)
GPIO.setmode(GPIO.BCM)
vibration_motor = vib.Vibration()
GPIO.setup(23, GPIO.OUT)  # 音声再生用のピン

# 音声再生の設定
pygame.mixer.init()
sound_effect = pygame.mixer.Sound('~~~~')

target = 5.0  # 加速度の基準値（例: 5 m/s^2） 

def detect_touch():
    #加速度データが基準値を超えたとき、魚が触れたとみなす
    acceleration = sensor.acceleration #センサーの加速度データ
    if acceleration[0] > target or acceleration[1] > target or acceleration[2] > target:
        return True
    return False

while True:
    if detect_touch():
        vibration_motor.motor_on()
        sound_effect.play()  # 音声を再生
        time.sleep(5)  # 振動と音声再生の時間
        vibration_motor.motor_off()
    time.sleep(0.1)  # センサーの読み取り間隔
