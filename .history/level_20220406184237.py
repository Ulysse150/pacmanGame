# Créé par leonardr, le 10/03/2022 en Python 3.7


import parametres
import pygame
from food import Consommable, Gomme, Pacgum
import random
from ghost import Ghost
from load_images import load


class Mur:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.s = parametres.tile_size
        self.rect = pygame.Rect(self.x * self.s, self.y *self.s, self.s, self.s)



    def draw(self):
        s = pygame.display.get_surface()
        pygame.draw.rect(s, (0,0,255), self.rect)







class Level:

    def __init__(self):
        self.image = pygame.image.load('sprites/map.png')
        self.image = pygame.transform.scale(self.image, (parametres.largeur_ecran, parametres.hauteur_ecran))
        #self.image = pygame.transform.scale(self.image)
        self.ghost_names = ['rouge','jaune','violet','bleu']


        #
        self.ghost_names = []
        self.murs = []
        self.gommes = []

        self.layout = self.load_layout()
        self.murs = self.load_walls(self.layout)
        self.load_gomme(self.layout)
        self.load_pacgum(self.layout)
        self.load_ghost()


        self.times = [0] * parametres.nb_fantomes
        self.score = 0




    def load_ghost(self):




        self.ghosts = []

        for n in self.ghost_names:
            spr = load(n)
            g = Ghost(11, 9, spr)
            self.ghosts.append(g)



    def gerer_coll(self, player):

        for g in self.gommes:
            if g.rect.colliderect(player.rect):


                if g.type == 'pacgomme':
                    player.venere()
                    self.score += 10
                elif g.type == 'gomme':
                    self.score += 30
                self.gommes.remove(g)


    def boucle(self, player):



        ecran = pygame.display.get_surface()



        #self.draw_lines(ecran)
        self.gerer_coll(player)




        ecran.blit(self.image, (0,0))
        for m in self.murs:
            pass
            #m.draw()

        for g in self.gommes:
            g.boucle()



        for g in self.ghosts:
            g.main(self.murs, self.layout, player.mode_venere)










    def draw_lines(self, e):

        for x in range(22):
            x1= x *( self.image.get_width() //21)
            pygame.draw.line(e, (255, 0,0), (x1, 0), (x1, parametres.hauteur_ecran))

        for x in range(20):
            y1= (self.image.get_width() //19)* x
            pygame.draw.line(e, (255, 0,0), (0, y1), (parametres.largeur_ecran , y1))


    def load_gomme(self, layout):
        nb = 0
        nb_pacgum=6



        for x in range(len(layout)):
            for y in range(len(layout[x])):
                if layout[x][y] == 0:
                    g = Gomme(y,x)




                    self.gommes.append(g)














    def load_layout(self):
        l = []
        with open('sprites/test.txt', 'r') as f:
            for line in f:
                ligne =[]
                for x in line:
                    if x != '\n':
                        ligne.append(int(x))
                l.append(ligne)

        return l



    def load_pacgum(self, layout):

        L1 = []

        for x in range(len(layout)):
            for y in range(len(layout[x])):
                if layout[x][y] in [0,0]:
                    L1.append([x, y])


        pos = []

        for x in range(parametres.pacg):
            n = random.randint(0, len(L1) - 1)
            pos.append(n)
            while n in pos:
                n = random.randint(0, len(L1) - 1)
            self.gommes.append(Pacgum(L1[n][1], L1[n][0]))





    def load_walls(self, layout):
        l =[]

        for x in range(len(layout)):
            for y in range(len(layout[x])):
                if layout[x][y] == 1:
                    p = Mur(y,x)

                    l.append(p)

        return l





