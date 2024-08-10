import time
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import pygame

# センサーとGPIOの設定
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # 振動モーターの接続ピン
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

#竿を振った時にも魚が釣れた判定されてしまうから、加速度じゃない方がいいかな、、？
#磁気センサーを反応しての方がいいかも　sensor.magnetic
#両方試す
#ボタン押したら判定開始にして、その間は強く振らないようにするとか
while True:
    if detect_touch():
        GPIO.output(18, GPIO.HIGH)  # 振動モーターをオン
        sound_effect.play()  # 音声を再生
        time.sleep(5)  # 振動と音声再生の時間
        GPIO.output(18, GPIO.LOW)  # 振動モーターをオフ
    time.sleep(0.1)  # センサーの読み取り間隔
