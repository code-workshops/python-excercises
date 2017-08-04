"""
Source: http://www.nerdparadise.com/programming/pygame/part3
"""
import pygame

pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play()
pygame.mixer.music.queue('new_song.mp3')
pygame.mixer.music.stop()

effect = pygame.mixer.Sound('beep.wav')
effect.play()
