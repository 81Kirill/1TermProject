import random

import pygame
from random import randint

pygame.init()

WIDTH, HEIDTH = 800, 900
widt, heit = 520, 800
rad = 15
FPS = 60


class Ball:
    def __init__(self, x, y, speedx, speedy, col):
        self.x, self.y = x, y
        self.col = col
        self.speedx, self.speedy = speedx, speedy
        self.speed = (self.speedx ** 2 + self.speedy ** 2) ** 0.5
        balls.append(self)

    def update(self):
        self.y += self.speedy
        self.x += self.speedx
        self.speed = (self.speedx ** 2 + self.speedy ** 2) ** 0.5
        if self.x - rad < (WIDTH // 2 - widt // 2) or self.x + rad > (WIDTH // 2 + widt // 2):
            self.speedx = -self.speedx
        if self.y - rad < (HEIDTH // 2 - heit // 2) or self.y + rad > (HEIDTH // 2 + heit // 2):
            self.speedy = -self.speedy
        if abs(self.speedx) >= 0.02:
            self.speedx -= 0.02 * self.speedx / self.speed
        else:
            self.speedx = 0
        if abs(self.speedy) >= 0.02:
            self.speedy -= 0.02 * self.speedy / self.speed
        else:
            self.speedy = 0

    def draw(self):
        pygame.draw.circle(window, self.col, (self.x, self.y), rad)


class Target:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(window, (100, 200, 50), (self.x, self.y), 33)


balls = []
targets = []
targets.append(Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2))
targets.append(Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2 - heit // 2 + 5))
targets.append(Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2 - heit // 2 + 5))
targets.append(Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2))
targets.append(Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2 + heit // 2 - 5))
targets.append(Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2 + heit // 2 - 5))

window = pygame.display.set_mode((WIDTH, HEIDTH))
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
k = 0
for i in range(0, 5):
    px = 330 + 32 * i
    balls[i] = Ball(px, 300, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(5, 9):
    px = 345 + 32 * (i - 5)
    balls[i] = Ball(px, 330, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(9, 12):
    px = 360 + 32 * (i - 9)
    balls[i] = Ball(px, 360, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(12, 14):
    px = 375 + 32 * (i - 12)
    balls[i] = Ball(px, 390, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(14, 15):
    px = 390 + 32 * (i - 14)
    balls[i] = Ball(px, 420, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(15, 16):
    balls[i] = Ball(390, 650, 0, 0, (255, 255, 255))
beat_next = len(balls) - 1
l = len(balls) - 1
mark = True
scored = False
p = 0

play = True
while play:
    window.fill(pygame.Color('black'))
    for i in range(len(balls)):
        if balls[i].speedx != 0:
            flag_stop = False
            break
        else:
            flag_stop = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            b1, b2, b3 = pygame.mouse.get_pressed()
            if b1 and flag_stop and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                balls[l].speedx = (mx - balls[l].x) * 0.03
                balls[l].speedy = (my - balls[l].y) * 0.03
                mark = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
            if flag_stop and (balls[-1].x != 390 and balls[-1].y != 650) and not (mark):
                beat_next = l
                balls[beat_next].col = (
                randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200))

                mx, my = pygame.mouse.get_pos()
                beat_next = l

                balls[beat_next].col = (
                randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200))
                for i in range(len(balls)):
                    if (balls[i].x - mx) ** 2 + (balls[i].y - my) ** 2 <= rad ** 2:
                        beat_next = i
                        break
                l = beat_next
                balls[beat_next].col = (255, 255, 255)

                mark = True



    for ball in balls:
        for target in targets:
            if (ball.x - target.x) ** 2 + (ball.y - target.y) ** 2 <= 27 ** 2 and ball != balls[l]:
                balls.remove(ball)
                l -= 1
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):
            if (balls[i].x - balls[j].x) ** 2 + (balls[i].y - balls[j].y) ** 2 <= 4 * rad ** 2:
                ax, ay = balls[i].x - balls[j].x, balls[i].y - balls[j].y
                nx, ny = -(balls[i].y - balls[j].y), balls[i].x - balls[j].x
                v1x, v1y = balls[i].speedx, balls[i].speedy
                v2x, v2y = balls[j].speedx, balls[j].speedy
                v1xcm, v1ycm = 0.5 * v1x - 0.5 * v2x, 0.5 * v1y - 0.5 * v2y
                v2xcm, v2ycm = 0.5 * v2x - 0.5 * v1x, 0.5 * v2y - 0.5 * v1y
                if nx != 0 and ny != 0:
                    balls[i].speedx = ((nx / ny * ay + ax) * v1xcm + 2 * v1ycm * ay) / (nx / ny * ay - ax) + 0.5 * (v1x + v2x)
                    balls[i].speedy = ((ny / nx * ax + ay) * v1ycm + 2 * v1xcm * ax) / (ny / nx * ax - ay) + 0.5 * (v1y + v2y)
                    balls[j].speedx = ((nx / ny * ay + ax) * v2xcm + 2 * v2ycm * ay) / (nx / ny * ay - ax) + 0.5 * (v1x + v2x)
                    balls[j].speedy = ((ny / nx * ax + ay) * v2ycm + 2 * v2xcm * ax) / (ny / nx * ax - ay) + 0.5 * (v1y + v2y)
                elif nx == 0:
                    balls[i].speedx = -v1x
                    balls[i].speedy = v1y
                    balls[j].speedx = -v2x
                    balls[j].speedy = v2y
                elif ny == 0:
                    balls[i].speedx = v1x
                    balls[i].speedy = -v1y
                    balls[j].speedx = v2x
                    balls[j].speedy = -v2y
    for ball in balls:
        ball.update()
    pygame.draw.rect(window, (21, 94, 20), (WIDTH // 2 - widt // 2, HEIDTH // 2 - heit // 2, widt, heit))
    for target in targets:
        target.update()
    for target in targets:
        target.draw()
    for ball in balls:
        ball.draw()



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
    for ball in balls:
        ball.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
