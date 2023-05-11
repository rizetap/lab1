import pygame, sys
import random, time

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
f1 = pygame.font.SysFont("Verdana", 30)
f2 = pygame.font.SysFont("Verdana", 30)

spd, scr, lvl = 5, 0, 1

class Snake:
    def __init__(self):
        self.x, self.y = 20, 20
        self.xdir, self.ydir = 0, 1
        self.head = pygame.Rect(self.x, self.y, 20, 20)
        self.body = [pygame.Rect(self.x-20, self.y, 20, 20)]
        self.dead = False
    
    def update(self):
        global food

        for cut in self.body:
            if self.head.x == cut.x and self.head.y == cut.y:
                self.dead = True
    
        if self.head.x > 500 or self.head.y > 500 or self.head.x < 0 or self.head.y < 0:
            self.dead = True

        if self.dead == True:
            quit()
            
        self.body.append(self.head)
    
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * 20
        self.head.y += self.ydir * 20
        self.body.remove(self.head)


class Food:
    def __init__(self):
        self.x = int(random.randint(0, 500)/20) * 20
        self.y = int(random.randint(0, 500)/20) * 20
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
    
    def update(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

snake = Snake()

food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if snake.ydir != -1:
                    snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                if snake.ydir != 1:
                    snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                if snake.xdir != -1:
                    snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                if snake.xdir != 1:
                    snake.xdir = -1

    snake.update()
    
    screen.fill((0,0,0))

    food.update()
    
    pygame.draw.rect(screen, (255, 255, 255), snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, (255, 255,255), square)

    if snake.head.x == food.x and snake.head.y == food.y:
        snake.body.append(pygame.Rect(square.x, square.y, 20, 20))
        scr+=1
        food = Food()
        if scr>=3 and scr%3==0: 
            lvl +=1
            spd +=1

    score = f1.render(f"Score: {scr}", True, (255,255,255))
    level = f2.render(f"Level: {lvl}", True, (255,255,255))

    screen.blit(score, (30,0))
    screen.blit(level, (300,0))

    pygame.display.flip()
    clock.tick(spd)

