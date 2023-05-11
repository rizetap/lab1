import pygame
pygame.init()

sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
sc.fill((0,0,0))

blank = eraser = (0,0,0)
green = (0,255,0)
blue = (0, 0, 255)
red = (255, 0, 0)

color = blank
pos = False
r = 15

def drawline(start, end, w, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    it = max(abs(dx), abs(dy))
    
    for i in range(it):
        pr = 1.0 * i / it
        apr = 1 - pr
        x = int(apr * start[0] + pr* end[0])
        y = int(apr * start[1] + pr * end[1])
        pygame.draw.circle(sc, color, (x, y), w)

def drawrect(mousepos, w, h, color):
    x = mousepos[0]
    y = mousepos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(sc, color, rect, 3)

def drawcircle(mousepos, color):
    x = mousepos[0]
    y = mousepos[1]
    pygame.draw.circle(sc, color, (x, y), 50, 3) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = red
            elif event.key == pygame.K_g:
                color = green
            elif event.key == pygame.K_b:
                color = blue
            elif event.key == pygame.K_e:
                color = eraser
            elif event.key == pygame.K_t:
                drawrect(pygame.mouse.get_pos(), 100, 90, color)
            elif event.key == pygame.K_c:
                drawcircle(pygame.mouse.get_pos(), color)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            if pos:
                stpos = pos
                endpos = pygame.mouse.get_pos()
                drawline(stpos, endpos, r, color)
                pos = endpos

    pygame.display.flip()
    clock.tick(60)