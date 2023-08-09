import pygame, sys
from pygame.locals import *
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
fontObj = pygame.font.Font('C:\Windows\Fonts\comic.ttf', 32)
total_kata = "Hello world!"
katakata = ""
index = 0
# warna = [WHITE, GREEN, BLUE]

while True: # main game loop 
    DISPLAYSURF.fill(WHITE)
    if index < 12:
        katakata += total_kata[index]
        textSurfaceObj = fontObj.render(katakata, True, GREEN, BLUE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 150)
        index +=1
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()