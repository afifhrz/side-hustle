import pygame
pygame.mixer.init()

soundObj = pygame.mixer.Sound('Pygame\mixkit-arcade-retro-game-over-213.wav')
soundObj.play()

import time
time.sleep(1) # wait and let the sound play for 1 second
soundObj.stop()