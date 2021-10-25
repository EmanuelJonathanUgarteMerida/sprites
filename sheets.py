import pygame as pg
import os

from pygame import image

from util import create_image_from_sheet


pg.init()
reloj=pg.time.Clock()
pantalla = pg.display.set_mode((400, 400))
sprite_sheet = pg.image.load(os.path.join("resources", "png", "megaman", "megaman.png")).convert_alpha()

x = 25
y = 20
width = 100
height = 100

imagenes = []

for frame in range(4):
    imagenes.append(create_image_from_sheet(sprite_sheet, frame, (x,y),width, height))
image=imagenes[0]
contador=0
pos=0    
game_over = False

while not game_over:
    reloj.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_over = True
    
    if contador==8:
        pos+=1
        if pos < len(imagenes):
            image=imagenes[pos]
        else:
            pos=0
            image=imagenes[pos]
        contador=0
    else:
        contador+=1


    pantalla.fill((0, 0, 0))
    pantalla.blit(image,image.get_rect().center)

    pg.display.flip()
