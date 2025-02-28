# Créé par fernana1, le 17/03/2022 en Python 3.7

import parametres
import pygame


class Ghost(pygame.sprite.Sprite):

    def __init__(self, x,y ):
        self.pos_x =x
        self.pos_y = y

        self.image = pygame.image.load('yellow.png')
        self.rect = self.image.get_rect(topleft = (x * parametres.tile_size, y  * parametres.tile_size))

    def ai(self):
        pass



    def main(self):
        s = pygame.display.get_surface()

        self.ai()

        s.blit(self.image, self.rect)







