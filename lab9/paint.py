import pygame
pygame.init()

sc = pygame.display.set_mode((500, 500))
sc.fill((0,0,0))
radius = 15

blank = eraser = (0,0,0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)

color = blank
pos = False

clock = pygame.time.Clock()

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

def drawsqr(mousepos, w, h, color):
    x = mousepos[0]
    y = mousepos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(sc, color, rect, 3)

def drawrtr(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x, y + 100),(x + 100, y + 100),]
    pygame.draw.polygon(sc, color, points, 3)

def draweqtr(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x - 50, y + 100),(x + 50, y + 100),]
    pygame.draw.polygon(sc, color, points, 3)  

def drawrom(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x - 50, y + 50),(x, y + 100),(x + 50, y + 50),]
    pygame.draw.polygon(sc, color, points, 3)

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
            elif event.key == pygame.K_v:
                draweqtr(color, pygame.mouse.get_pos())
            elif event.key == pygame.K_q:
                drawsqr(pygame.mouse.get_pos(), 100, 100, color)
            elif event.key == pygame.K_o:
                drawrtr(color, pygame.mouse.get_pos())
            elif event.key == pygame.K_v:
                drawrom(color, pygame.mouse.get_pos())
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            if pos:
                stpos = pos
                endpos = pygame.mouse.get_pos()
                drawline(stpos, endpos, radius, color)
                pos = endpos

    pygame.display.flip()
    clock.tick(60)
