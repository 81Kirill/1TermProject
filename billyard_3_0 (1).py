import random
import Balls
import pygame
from random import randint

pygame.init()

WIDTH, HEIDTH = 800, 900
widt, heit = 520, 800
rad = 15
FPS = 60





class Target:
    def __init__(self, x, y):
        self.x, self.y = x, y
        targets.append(self)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(window, (100, 200, 50), (self.x, self.y), 33)



"""Прорисовка поля и лунок"""
targets = []
Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2)
Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2 - heit // 2 + 5)
Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2 - heit // 2 + 5)
Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2)
Target(WIDTH // 2 - widt // 2 + 5, HEIDTH // 2 + heit // 2 - 5)
Target(WIDTH // 2 + widt // 2 - 5, HEIDTH // 2 + heit // 2 - 5)

window = pygame.display.set_mode((WIDTH, HEIDTH))
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)



"""Начальное расположение шаров"""
for i in range(0, 5):
    px = 330 + 32 * i
    Balls.Ball(px, 300, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(5, 9):
    px = 345 + 32 * (i - 5)
    Balls.Ball(px, 330, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(9, 12):
    px = 360 + 32 * (i - 9)
    Balls.Ball(px, 360, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(12, 14):
    px = 375 + 32 * (i - 12)
    Balls.Ball(px, 390, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(14, 15):
    px = 390 + 32 * (i - 14)
    Balls.Ball(px, 420, 0, 0,
                    (randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200)))
for i in range(15, 16):
    Balls.Ball(390, 650, 0, 0, (255, 255, 255))
beat_next = len(Balls.balls) - 1
l = len(Balls.balls) - 1
"""Когда выбран биток mark = True"""
mark = True
scored = False
p = 0

play = True
while play:
    window.fill(pygame.Color('black'))
    for i in range(len(Balls.balls)):
        """Проверка на остновку всех шаров"""
        if Balls.balls[i].speedx != 0:
            flag_stop = False
            break
        else:
            flag_stop = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            """Удар битком"""
            b1, b2, b3 = pygame.mouse.get_pressed()
            if b1 and flag_stop and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                Balls.balls[l].speedx = (mx - Balls.balls[l].x) * 0.03
                Balls.balls[l].speedy = (my - Balls.balls[l].y) * 0.03
                mark = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
            """Выбор нового битка в начале следующего хода"""
            if flag_stop and (balls[-1].x != 390 and balls[-1].y != 650) and not (mark):
                beat_next = l
                """меняем цвет бывшего битка"""
                balls[beat_next].col = (
                randint(40, 200), random.choice([randint(0, 75), randint(115, 255)]), randint(40, 200))

                mx, my = pygame.mouse.get_pos()
                """Нажатием мыши выбираем биток"""
                for i in range(len(balls)):
                    if (balls[i].x - mx) ** 2 + (balls[i].y - my) ** 2 <= rad ** 2:
                        beat_next = i
                        break
                l = beat_next
                balls[beat_next].col = (255, 255, 255)

                mark = True


    """Падение шара в лунку"""
    for ball in Balls.balls:
        for target in targets:
            if (ball.x - target.x) ** 2 + (ball.y - target.y) ** 2 <= 27 ** 2 and ball != Balls.balls[l]:
                Balls.balls.remove(ball)
                l -= 1

    """Столкновение двух шаров"""
    for i in range(0, len(Balls.balls)):
        for j in range(i + 1, len(Balls.balls)):
            if (Balls.balls[i].x - Balls.balls[j].x) ** 2 + (Balls.balls[i].y - Balls.balls[j].y) ** 2 <= 4 * 15 ** 2:
                ax, ay = Balls.balls[i].x - Balls.balls[j].x, Balls.balls[i].y - Balls.balls[j].y
                nx, ny = -(Balls.balls[i].y - Balls.balls[j].y), Balls.balls[i].x - Balls.balls[j].x
                v1x, v1y = Balls.balls[i].speedx, Balls.balls[i].speedy
                v2x, v2y = Balls.balls[j].speedx, Balls.balls[j].speedy
                v1xcm, v1ycm = 0.5 * v1x - 0.5 * v2x, 0.5 * v1y - 0.5 * v2y
                v2xcm, v2ycm = 0.5 * v2x - 0.5 * v1x, 0.5 * v2y - 0.5 * v1y

            # Защита от залипания
                if (((Balls.balls[i].speedx - Balls.balls[j].speedx) ** 2 + (Balls.balls[i].speedy - Balls.balls[j].speedy) ** 2) ** 0.5 < 10):
                    Balls.balls[i].x += ax / 100
                    Balls.balls[i].y += ay / 100
                    Balls.balls[j].x += -ax / 100
                    Balls.balls[j].y += -ay / 100

                if (Balls.balls[i].x - Balls.balls[j].x) ** 2 + (Balls.balls[i].y - Balls.balls[j].y) ** 2 <= 4 * 15 ** 2:
                    if nx != 0 and ny != 0:
                        Balls.balls[i].speedx = ((nx / ny * ay + ax) * v1xcm + 2 * v1ycm * ay) / (nx / ny * ay - ax) + 0.5 * (
                                    v1x + v2x)
                        Balls.balls[i].speedy = ((ny / nx * ax + ay) * v1ycm + 2 * v1xcm * ax) / (ny / nx * ax - ay) + 0.5 * (
                                    v1y + v2y)
                        Balls.balls[j].speedx = ((nx / ny * ay + ax) * v2xcm + 2 * v2ycm * ay) / (nx / ny * ay - ax) + 0.5 * (
                                    v1x + v2x)
                        Balls.balls[j].speedy = ((ny / nx * ax + ay) * v2ycm + 2 * v2xcm * ax) / (ny / nx * ax - ay) + 0.5 * (
                                    v1y + v2y)
                    elif nx == 0:
                        Balls.balls[i].speedx = -v1x
                        Balls.balls[i].speedy = v1y
                        Balls.balls[j].speedx = -v2x
                        Balls.balls[j].speedy = v2y
                    elif ny == 0:
                        Balls.balls[i].speedx = v1x
                        Balls.balls[i].speedy = -v1y
                        Balls.balls[j].speedx = v2x
                        Balls.balls[j].speedy = -v2y


    for ball in Balls.balls:
        ball.update()
    pygame.draw.rect(window, (21, 94, 20), (WIDTH // 2 - widt // 2, HEIDTH // 2 - heit // 2, widt, heit))
    for target in targets:
        target.update()
    for target in targets:
        target.draw()
    for ball in Balls.balls:
        ball.draw()



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()