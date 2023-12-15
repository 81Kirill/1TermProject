balls = []
import pygame
rad = 15
WIDTH, HEIDTH = 800, 900
widt, heit = 520, 800
rad = 15
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIDTH))
class Ball:
    def __init__(self, x, y, speedx, speedy, col):
        self.x, self.y = x, y
        self.col = col
        self.speedx, self.speedy = speedx, speedy
        balls.append(self)

    """Движение шара за кадр прорисовки"""
    def update(self):
        self.y += self.speedy
        self.x += self.speedx
        self.speed = (self.speedx ** 2 + self.speedy ** 2) ** 0.5
        """столкновение с бортом"""
        if self.x - rad < (WIDTH // 2 - widt // 2) or self.x + rad > (WIDTH // 2 + widt // 2):
            self.speedx = -self.speedx
        if self.y - rad < (HEIDTH // 2 - heit // 2) or self.y + rad > (HEIDTH // 2 + heit // 2):
            self.speedy = -self.speedy
        """трение"""
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