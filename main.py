import pygame as pg

class Player:
    def __init__(self, colour, pos, size, speed_x, speed_y):
        self.img = pg.Surface(size)
        self.img.fill(colour)
        self.pos = pos
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        screen.blit(self.img, self.pos)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

screen_width = 800
screen_height = 900
pg.init()
screen = pg.display.set_mode([screen_width, screen_height])

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BLACK)
    pg.display.flip()
    clock.tick(60)
