import pygame as pg
import os
def create_image_from_sheet(sprite_sheet,frame,point,width,height):
    image=pg.Surface((width,height)).convert_alpha()
    x=(frame*width)+point[0]

    image.blit(sprite_sheet, (0,0), (x,point[1], width, height))
    image.set_colorkey((255,255,25))
    return image