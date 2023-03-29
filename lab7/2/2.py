import pygame
from pygame import mixer
pygame.init()
mixer.init()

sc = pygame.display.set_mode((400,400)) 
pygame.display.set_caption("Spotify")
clock = pygame.time.Clock()
bg = pygame.image.load("player.jpg")
bg = pygame.transform.scale(bg, (400, 400))

songs = ['dajte_tank(!)_vy.mp3', 'dajte_tank(!)_my.mp3', 'dajte_tank(!)_ya.mp3']

n = 0
csong = pygame.mixer.music.load(songs[n])
pygame.mixer.music.play()
pygame.mixer.music.pause()

font = pygame.font.SysFont("segoeuihistoric", 24, True)

ch = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        #остановка    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ch:
                    pygame.mixer.music.unpause()
                    ch = False
                else:
                    pygame.mixer.music.pause()
                    ch = True
            #следующая       
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                if n<2: n+=1
                else: n =0 
                pygame.mixer.music.load(songs[n])
                pygame.mixer.music.play()
                if ch:
                    pygame.mixer.music.pause()

            if event.key == pygame.K_LEFT: 
                pygame.mixer.music.stop()
                if n>0: n-=1 
                else: n = 2
                pygame.mixer.music.load(songs[n])
                pygame.mixer.music.play()
                if ch:
                    pygame.mixer.music.pause()

    sc.blit(bg, (0,0))

    sg = songs[n]
    songname = sg.replace(".mp3", "")
    text = font.render(songname, True, (0,0,0))
    sc.blit(text, (110,90))
    
    pygame.display.flip()
    clock.tick(60)