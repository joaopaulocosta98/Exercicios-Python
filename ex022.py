import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
