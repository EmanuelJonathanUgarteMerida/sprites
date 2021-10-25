import pygame as pg
import os


def cargar_img(name):
    img = pg.image.load(os.path.join('resources', 'png', name+'.png'))
    img = pg.transform.scale(img, (150, 150))
    img.get_rect().center=(350, 250)
    return img


pg.init()
seguir = True
screen = pg.display.set_mode((700, 500))

clock = pg.time.Clock()
counter = 0
image_pos = 0
dinos = []
for x in range(1, 8):
    dinos.append(cargar_img(f'Run ({x})'))

image = dinos[image_pos]
image_rect = image.get_rect()

while seguir:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                seguir = False

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        image_rect.x -= 1
    elif pressed[pg.K_RIGHT]:
        image_rect.x += 1
        if counter == 2:
            image = dinos[image_pos]
            image_pos += 1
            if image_pos == len(dinos):
                image_pos = 0
            counter = 0
        else:
            counter += 1

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pg.display.flip()
