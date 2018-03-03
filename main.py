import pygame as pg

vec = pg.math.Vector2

class Player:
    def __init__(self, colour, pos, size, velocity):
        self.img = pg.Surface(size)
        self.img.fill(colour)
        self.pos = pos
        self.vel = velocity

    def draw(self):
        screen.blit(self.img, self.pos)

    def update(self, dt):
        self.keys_pressed()
        self.pos += self.vel * dt / 1000
        self.vel -= self.vel * 5 * dt / 1000

    def keys_pressed(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -150
        if keys[pg.K_d]:
            self.vel.x = 150
        

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

screen_width = 800
screen_height = 900
pg.init()
screen = pg.display.set_mode([screen_width, screen_height])

player = Player(WHITE, vec(300, 300), (30, 30), vec(0, 0))

running = True
clock = pg.time.Clock()
dt = 0


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    player.update(dt)
    screen.fill(BLACK)
    player.draw()
    pg.display.flip()
    dt = clock.tick(60)
