"""
Source: http://www.nerdparadise.com/programming/pygame/part3
"""
import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load('media/marbles.mp3')
pygame.mixer.music.play(0)
time.sleep(5)
pygame.mixer.music.stop()

try:
    effect = pygame.mixer.Sound('media/bye.wav')
except MemoryError as e:
    raise
else:
    effect.play()
    time.sleep(2)
