import matplotlib.pyplot as plt
import numpy as np
import pygame as pg

pg.init()

listX = []
listY = []
fps = 60
clock = pg.time.Clock()
vx = np.random.uniform(-10, 10, 1)
vy = np.random.uniform(-10, 10, 1)
v = 0
px = 100
py = 100
maxX = 700
minX = 0
maxY = 700
minY = 1
p = (px, py)
screen = pg.display.set_mode([maxX, maxY])
running = True


def update_px(px):
    px = px + vx
    return (px)


def update_py(py):
    py = py + vy
    return py


def collision_x(x, vx):
    if x >= maxX - 10:
        x = maxX
        vx = vx - vx * 2
    if x <= minX + 10:
        x = minX
        vx = vx - vx * 2
    return vx


def collision_y(y, vy):
    if y >= maxY - 5:
        y = maxY
        vy = vy - vy * 2
    if y <= minY + 5:
        y = minY
        vy = vy - vy * 2
        vy - 10
    return vy


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    vy = vy + 0.163
    px = update_px(px)
    py = update_py(py)
    vx = collision_x(px, vx)
    vy = collision_y(py, vy)
    listX.append(px)
    listY.append(-py)
    clock.tick(fps)
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (0, 0, 255), (px, py), 10)
    pg.display.flip()

plt.scatter(listX, listY)
plt.show()
