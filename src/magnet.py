#磁石センサーによる竿の操作
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
import vibration as vib
import music as mus

# SENSOR PIN
PIN_MAGNET = 21

def main():
    # ピンを入力に設定(プルアップ設定)
    factory = PiGPIOFactory()
    magnet = Button(PIN_MAGNET, pull_up=True, bounce_time=0.3, pin_factory=factory) #最初の変更があってから、状態の変更を無視する時間をbounce_timeで秒単位で指定
    vibration_motor = vib.Vibration()
    music = mus.Music(music_file="~~~~")

    def stick():
        vibration_motor.motor_off()
        music.music_off()
        print("magnets stick")

    def leave():
        vibration_motor.motor_on() 
        music.music_on() 
        print("magnets leave")

    magnet.when_pressed = stick
    magnet.when_released = leave
    pause()

    return

if __name__ == "__main__": #直接このシートを実行したらmain()を動かすようにする。スクリプトを他のモジュールとしてインポートした場合、動作部分が自動的に実行されることを防ぐことができる。
    main()
