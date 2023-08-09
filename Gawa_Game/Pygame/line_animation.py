import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1600, 800), 0, 32)
pygame.display.set_caption('Line Animation')

WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
linex = 10
liney = 10
end_pos1 = [linex, liney]
end_pos2 = [280, 10]
end_pos3 = [280, 220]
end_pos4 = [10, 220]

status_pict = [True, False, False, False]

direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    
    if status_pict[0]:
        pygame.draw.line(DISPLAYSURF, BLUE, (linex, liney), end_pos1, 4)
    
    if status_pict[1]:
        pygame.draw.line(DISPLAYSURF, BLUE, (280, liney), end_pos2, 4)
        
    if status_pict[2]:
        pygame.draw.line(DISPLAYSURF, BLUE, (280, 220), end_pos3, 4)
        
    if status_pict[3]:
        pygame.draw.line(DISPLAYSURF, BLUE, (10, 220), end_pos4, 4)
        
        
    if direction == 'right':
        end_pos1[0] += 5
        if end_pos1[0] == 280:
            direction = 'down'
            status_pict[1] = True
    elif direction == 'down':
        end_pos2[1] += 5
        if end_pos2[1] == 220:
            direction = 'left'
            status_pict[2] = True
    elif direction == 'left':
        end_pos3[0] -= 5
        if end_pos3[0] == 10:
            direction = 'up'
            status_pict[3] = True
    elif direction == 'up':
        end_pos4[1] -= 5
        if end_pos4[1] == 10:
            direction = 'mati'

    # DISPLAYSURF.blit(catImg, (catx, caty))
    # pixObj = pygame.PixelArray(DISPLAYSURF)
    # pixObj[480][380] = BLACK
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)