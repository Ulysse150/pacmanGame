# Créé par leonardr, le 10/03/2022 en Python 3.7


import parametres
import pygame



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
        #self.image = pygame.transform.scale(self.image, (parametres.largeur_ecran, parametres.hauteur_ecran))
        self.image = pygame.transform.scale2x(self.image)

        self.murs = []

        self.layout = self.load_layout()
        self.murs = self.load_walls(self.layout)



    def boucle(self):



        ecran = pygame.display.get_surface()


        #ecran.blit(self.image, (0,0))
        #self.draw_lines(ecran)
        for m in self.murs:
          m.draw()

    def draw_lines(self, e):

        for x in range(22):
            x1= x *( self.image.get_width() //21)
            pygame.draw.line(e, (255, 0,0), (x1, 0), (x1, parametres.hauteur_ecran))

        for x in range(20):
            y1= (self.image.get_width() //19)* x
            pygame.draw.line(e, (255, 0,0), (0, y1), (parametres.largeur_ecran , y1))






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
    def load_walls(self, layout):
        l =[]

        for x in range(len(layout)):
            for y in range(len(layout[x])):
                if layout[x][y] == 1:
                    p = Mur(y,x)

                    l.append(p)

        return l

    def points(self):
        screen = pygame.display.get_surface()
        l=self.layout()
        for i in range (len(l)):
            for j in range (len(l[0])):
                if l[i][j]==0:
                    pygame.draw.rect(screen,(100,100,0),3,3,l[i],l[0][j])



