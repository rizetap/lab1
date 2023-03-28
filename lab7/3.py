import pygame 
pygame.init()

sc =pygame.display.set_mode((600, 400))
pygame.display.set_caption("domalaq")

x, y= 0, 0
clock=pygame.time.Clock()
while True: 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            quit()
    clock.tick(60)
    bt=pygame.key.get_pressed()
    if bt[pygame.K_UP]: y-=20
    if bt[pygame.K_DOWN]: y+=20
    if bt[pygame.K_LEFT]: x-=20
    if bt[pygame.K_RIGHT]: x+=20
    if x+25>600: x=575
    if x-25<0: x=25
    if y+25>400: y=375
    if y-25<0: y=25

    sc.fill((255, 255, 255))
    pygame.draw.circle(sc, (255,0,0), (x, y), 25)
    pygame.display.flip()