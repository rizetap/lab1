import pygame, sys
from pygame.locals import *
import random, time
pygame.init()

spd, cspd = 5, 5
scr, cscr = 0, 0
font1 = pygame.font.SysFont("Verdana", 60)
font2 = pygame.font.SysFont("Verdana", 20)
game_over = font1.render("Game Over", True, (0,0,0))

bg = pygame.image.load("AnimatedStreet.png")
sc = pygame.display.set_mode((400,600))
pygame.display.set_caption("Race")
sc.fill((255,255,255))
clock = pygame.time.Clock()

class Coin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        global cscr
        self.rect.move_ip(0, cspd)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)


class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        global cscr
        self.rect.move_ip(0, cspd)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)
    def move(self):
        global scr
        self.rect.move_ip(0,spd)
        if (self.rect.bottom > 600):
            scr +=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        bt = pygame.key.get_pressed()
        if self.rect.left > 0:
            if bt[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 400:
            if bt[K_RIGHT]:
                self.rect.move_ip(5,0)

p1 = Player()
e1 = Enemy()
c1 = Coin1()
c2 = Coin2()

enems = pygame.sprite.Group()
enems.add(e1)
coins1 = pygame.sprite.Group()
coins1.add(c1)
coins2 = pygame.sprite.Group()
coins2.add(c2)
all = pygame.sprite.Group()
all.add(p1)
all.add(e1)
all.add(c1)
all.add(c2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == INC_SPEED:
            if cscr == 40: 
                spd +=2
                cspd += 0.5

    sc.blit(bg, (0,0))
    scrs = font2.render(str(scr), True, (0,0,0))
    sc.blit(scrs, (10,10))
    c_scrs = font2.render("Coins: " + str(cscr), True, (0,0,0))
    sc.blit(c_scrs, (300, 10))

    for entity in all:
        entity.move()
        sc.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(p1, enems):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        sc.fill((255,0,0))
        sc.blit(game_over, (30,250))
        sc.blit(c_scrs, (30,330))
        pygame.display.flip()

        for entity in all:
            entity.kill()
        time.sleep(2)

    if pygame.sprite.spritecollideany(p1, coins1):
        cscr += 1
        c1.rect.top = 0
        c1.rect.center = (random.randint(40,360), 0)

    if pygame.sprite.spritecollideany(p1, coins2):
        cscr += 3
        c2.rect.top = 0
        c2.rect.center = (random.randint(40,360), 0)

    pygame.display.flip()
    clock.tick(60)
