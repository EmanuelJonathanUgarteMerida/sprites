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
imagenes_correr=[]

for frame in range(4):
    imagenes.append(create_image_from_sheet(sprite_sheet, frame, (x,y),width, height))
imagen=imagenes[0]
contador=0
pos=0

x=434
y=0
width=101
height=116
for frame in range(6):
    imagenes_correr.append(create_image_from_sheet(sprite_sheet,frame,(x,y),width,height))
image_correr=imagenes_correr[0]   
contador_c=0
pos_c=0
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
            imagen=imagenes[pos]
        else:
            pos=0
            imagen=imagenes[pos]
        contador=0
    else:
        contador+=1

    if contador_c==8:
        pos_c+=1
        if pos_c < len(imagenes_correr):
            image_correr=imagenes_correr[pos_c]
        else:
            pos_c=0
            image_correr=imagenes_correr[pos_c]
        contador_c=0
    else:
        contador_c+=1


    pantalla.fill((255, 255, 255))
    pantalla.blit(imagen,imagen.get_rect().center)
    pantalla.blit(image_correr,(200,200))
    pg.display.flip()
