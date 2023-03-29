import pygame
import datetime
pygame.init()

sc = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
#вставка изображений
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (600, 450))
hmin = pygame.image.load('minutes.png')
hmin = pygame.transform.scale(hmin, (600, 450))
hsec = pygame.image.load('seconds.png')
hsec = pygame.transform.scale(hsec, (600, 450))

#функция для кручения
def rotate(img, ang):
    rt = pygame.transform.rotate(img, ang)
    rec = rt.get_rect()
    rec.center = (300,225)
    sc.blit(rt, rec)


while True:
        #время
        t = datetime.datetime.now()
        min = t.minute
        sec = t.second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        sc.blit(bg, (0, 0))
        rotate(hmin, -(min*6))
        rotate(hsec, -(sec*6))
        
        pygame.display.flip()
        clock.tick(60)
    
    