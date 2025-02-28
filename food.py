# Créé par leonardr, le 15/03/2022 en Python 3.7
import pygame
import parametres


class Consommable(pygame.sprite.Sprite):

    def __init__(self, x,y, image, type):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.image = image
        self.type = type

        x1 = int(x *parametres.tile_size + (parametres.tile_size //2))
        y1 = int(y *parametres.tile_size + (parametres.tile_size //2))


        self.rect = self.image.get_rect(center = (x1, y1))

    def boucle(self):
        s = pygame.display.get_surface()
        self.main()
        if not([self.pos_x, self.pos_y] in [ [11, 7], [11, 11]]):
            s.blit(self.image, self.rect)

    def main(self):
        pass





class Gomme(Consommable):
    def __init__(self, x, y):
        img = pygame.image.load('sprites/gomme.png')
        img = pygame.transform.scale(img, (5,5))

        super().__init__( x, y, img, 'gomme')



class Pacgum(Consommable):
    def __init__(self, x, y):
        img = pygame.image.load('sprites/pac_gum.png')
        img = pygame.transform.scale(img, (20, 20))

        super().__init__( x, y, img, 'pacgomme')







