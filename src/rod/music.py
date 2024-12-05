import RPi.GPIO as GPIO
import pygame

class Music:
    def __init__(self, PIN_MUSIC=23, music_file="~~~~"):
        self.PIN_MUSIC = PIN_MUSIC
        self.music_file = music_file
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_MUSIC, GPIO.OUT)

        # Pygame初期化
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)

    def music_on(self):
        GPIO.output(self.PIN_MUSIC, GPIO.HIGH)
        pygame.mixer.music.play()
        print("音楽を再生します")

    def music_off(self):
        GPIO.output(self.PIN_MUSIC, GPIO.LOW)
        pygame.mixer.music.stop()
        print("音楽を停止します")


