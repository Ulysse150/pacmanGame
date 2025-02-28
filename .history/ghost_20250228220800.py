# Créé par fernana1, le 17/03/2022 en Python 3.7
from numpy import newaxis
import pygame
import random
import parametres
import time


class Ghost:

    def __init__(self,x ,y, images = []):
        self.x = x
        self.y = y


        self.images = images


        self.image = pygame.image.load('sprites/yellow.png')
        self.rect = self.image.get_rect(topleft =(x * parametres.tile_size, y *parametres.tile_size))
        self.direction = 'right'
        self.old_pos = self.rect.topleft
        self.old = [x,y]
        self.font = pygame.font.SysFont("comicsansms", 20)
        self.a = self.font.render('n', True, (255,255,255), (0,0,0))

        self.scared_image = pygame.image.load('sprites/scared.png')
        self.scared_image = pygame.transform.scale(self.scared_image, (35, 35))
        self.moving = True

        self.o_image = self.image

        self.dead = False
        self.time_dead = 0
        self.speed =  1.4
        self.mode = 'moving'

        self.pos = []
        self.old_po = []
    def determine_pos(self):
        self.x = self.rect.x // parametres.tile_size
        self.y = self.rect.y // parametres.tile_size


        if self.direction == 'up':
            self.y = self.rect.bottom // parametres.tile_size

        elif self.direction == 'left':
            self.x = self.rect.right // parametres.tile_size





        t = parametres.tile_size
        s= pygame.display.get_surface()
        """
        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*self.y), (t *(self.x+1), t*self.y        ))

        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*self.y), (t *(self.x), t*(self.y+1)        ))

        pygame.draw.line(s, (255, 0,0) , (t *( self.x+1) , t*self.y), (t *(self.x+1), t*(self.y+1)        ))

        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*(self.y+1)), (t *(self.x+1), t*(self.y +1)       ))
        """

    def collide(self, plateformes):

        for p in plateformes:
            if self.rect.colliderect(p.rect):
                self.rect.topleft = self.old_pos
                return True


    def where_can_go(self, layout):
        self.determine_pos()


        x = self.x
        y = self.y

        rep = []
        #on teste à gauche


        if y < 0 or y >= len(layout):


            if self.direction == 'down':
                self.rect.top = 1
            elif self.direction == 'up':
                self.rect.bottom = parametres.hauteur_ecran - 1

            return rep


        if x-1 >0:
            if layout[y][x-1] ==0 :
                rep.append('left')
        if x+1 <len(layout[0]):

            if layout[y][x+1] ==0 :
                rep.append('right')
        if y-1 >0:
            if layout[y-1][x] ==0 :
                rep.append('up')

        if y+1 < len(layout):
            if layout[y+1][x] ==0 :
                rep.append('down')

        return rep

    def die(self):
        self.dead = True
        self.time_dead = pygame.time.get_ticks()



    def croisement(self, layout):
        possibilies = self.where_can_go(layout)

        if self.direction in possibilies:
            possibilies.remove(self.direction)


        if parametres.contraires[self.direction] in possibilies:
            possibilies.remove(parametres.contraires[self.direction])
        return len(possibilies) > 0



    def ai(self, plateformes, layout, scared):
        if not(self.dead):
            self.determine_pos()


            self.old_directions = self.where_can_go(layout)
            self.old = [self.x, self.y]
            self.move()


            self.determine_pos()




            self.new =[]
            s = self.collide(plateformes)
            if [self.x, self.y] != self.old:

                self.pos = self.where_can_go(layout)

                if self.croisement(layout):
                    self.mode = 'moving'
                else:
                    self.mode = 'choosing'

                for direc in self.pos:
                    if not(direc in [parametres.contraires.get(self.direction)]):
                        self.new.append(direc)


                if len(self.new) >0:


                    self.i = random.randint(0, len(self.new) - 1)

                    self.direction =self.new[self.i]
            else:
                self.mode = 'moving'










        else:
            if pygame.time.get_ticks() > self.time_dead + 2500:
                self.dead = False
                self.x = 11
                self.y = 9
                self.rect.x = self.x * parametres.tile_size
                self.rect.y = self.y * parametres.tile_size
                self.direction = 'right'
        if scared :
            self.image = self.scared_image
        else:
            self.image = self.o_image





    def move(self):

        if self.direction == 'right':
            self.rect.x += self.speed
            self.o_image = self.images.get('droite.png')



        elif self.direction == 'left':
            self.rect.x += -self.speed
            self.o_image = self.images.get('gauche.png')

        elif self.direction == 'up':
            self.rect.y += -self.speed
            self.o_image = self.images.get('haut.png')

        elif self.direction == 'down':
            self.rect.y += self.speed
            self.o_image = self.images.get('bas.png')



    def main(self, plateformes, layout, scared):


        self.old_p = self.where_can_go(layout)
        s = pygame.display.get_surface()
        self.old_pos = self.rect.topleft

        self.ai(plateformes, layout, scared)
        if not(self.dead):
            s.blit(self.image, self.rect)
