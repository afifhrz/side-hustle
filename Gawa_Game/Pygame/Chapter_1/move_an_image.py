import sys, pygame
pygame.init()
SPRITE_HEIGHT = 10
SPRITE_WIDTH = 10
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > 800:
            self.pos.left = 0
        if self.pos.top > 800-SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = 1600
        if self.pos.top < 0:
            self.pos.top = 800-SPRITE_HEIGHT
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('Pygame/Chapter_1/player.bmp').convert()
player = pygame.transform.scale(player, (50, 50))
entity = pygame.image.load('Pygame/Chapter_1/alien1.bmp').convert()
entity = pygame.transform.scale(entity, (40, 50))
background = pygame.image.load('Pygame/Chapter_1/background.bmp').convert()
background = pygame.transform.scale(background, (1600, 800))
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 50, 1)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    # screen.blit(background, p.pos, p.pos)
    screen.blit(p.image, p.pos)
    pygame.display.update()
    clock.tick(60)