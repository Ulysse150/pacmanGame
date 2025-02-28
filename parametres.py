# Créé par leonardr, le 08/03/2022 en Python 3.7
import pygame
tile_size = 37

largeur_ecran =  21 * tile_size

hauteur_ecran = 19 * tile_size

hauteur_map = 19

larg_map = 21

animation_s = 0.07
sprites = { 'right': 2, 'left' : 2 , 'down' : 2, 'up':2


}

pos_texte = (280, 550)


contraires = {    'right': 'left', 'left' : 'right', 'up':'down', 'down': 'up'}

red = (200, 10, 10)
bleu = (37, 253, 233)



nb_fantomes = 4
ghost = [[11,9]]

pacg  = 7
nb_vies = 5

def resize(image, h):
    hauteur = image.get_height()
    largeur = image.get_width()

    rap = largeur / hauteur

    new_h = int(h)
    new_l = int(h * rap)
    return pygame.transform.scale(image, (new_l, new_h))

