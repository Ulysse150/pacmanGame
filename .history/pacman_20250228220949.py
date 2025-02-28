# Créé par leonardr, le 08/03/2022 en Python 3.7

from re import M





import pygame
import parametres
import time

pygame.init()


class Pacman(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()


        self.image = pygame.image.load("sprites\\pacman_1.png")
        self.x_pos = x
        self.y_pos = y
        self.direction = 'right'
        self.image = pygame.transform.scale(self.image, (35 , 35))

        self.rect = self.image.get_rect(topleft = (self.x_pos * parametres.tile_size, self.y_pos * parametres.tile_size))
        self.vitesse = 1
        self.speed_x = 0
        self.speed_y = 0
        self.determine_pos()
        self.old_location = [self.x_pos, self.y_pos]
        

        self.font = pygame.font.SysFont("comicsansms", 25)

        self.colliding = False
        self.mur_co = None
        self.index = 0
        self.load_images()
        self.pos_affiche = self.font.render('Score : 0', True, (0,0,0), (255,255,255))

        self.mode_venere = False

        self.temps_venere = 5

        self.last_time = 0
        self.vies = parametres.nb_vies

        self.dead = False
        self.pac_affiche = self.font.render('Lifes remaining : %s' % self.vies, True,  (255, 255, 255))

        #print(self.images)


    def move(self, direction):

        if direction == 'left':

            self.speed_x = -0.75
            self.speed_y = 0

        elif direction == 'right':



            self.speed_x = 1.5
            self.speed_y = 0

        elif direction == 'up':

            self.speed_x = 0
            self.speed_y = -0.75

        elif direction == 'down':

            self.speed_x = 0
            self.speed_y = 1.5


        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <=0 and self.direction == 'up':
            self.rect.y = parametres.hauteur_ecran

    def save_location(self):
        self.old_location = [self.x_pos, self.y_pos]






    def load_images(self):
        self.images = {}
        for key in parametres.sprites:
            l=[]
            for x in range(parametres.sprites[key]):
                path = 'sprites/pac/%s_%s.png' % (key, x)
                l.append(pygame.image.load(path))

            self.images[key] = l

    def dessiner_hitbox(self):
        s = pygame.display.get_surface()
        pygame.draw.line(s, (255,0,0), (self.rect.x, self.rect.y), (self.rect.right, self.rect.top))
        pygame.draw.line(s, (255,0,0), (self.rect.x, self.rect.bottom), (self.rect.right, self.rect.bottom))
        pygame.draw.line(s, (255,0,0), (self.rect.x, self.rect.y), (self.rect.x, self.rect.bottom))
        pygame.draw.line(s, (255,0,0), (self.rect.right, self.rect.y), (self.rect.right, self.rect.bottom))

    def get_input(self, level):

        key = pygame.key.get_pressed()
        self.determine_pos()
        positions = self.where_can_go(level.layout)
        if key[pygame.K_RIGHT]:
            if 'right' in positions:

                self.direction = 'right'


        elif key[pygame.K_LEFT]:

            if 'left' in positions:
                self.direction = 'left'

        elif key[pygame.K_UP]:
            if 'up' in positions:
                self.direction = 'up'

        elif key[pygame.K_DOWN]:


            if 'down' in positions:
                self.direction = 'down'



    def died(self, level):
        #print('pacman est mort de mort mortelle.')
        time.sleep(0.75)

        level.load_ghost()



        self.x_pos = 1
        self.y_pos = 1
        self.rect.topleft = (38, 38)


        self.direction = 'right'
        self.vies -=1



    def collision_fantomes(self, level):
        ghosts = level.ghosts.copy()
        for ghost in ghosts:
            if self.rect.colliderect(ghost.rect):

                if self.mode_venere:
                    if not(ghost.dead):
                        level.score += 50
                    ghost.die()


                else:
                    if not(ghost.dead):
                        self.died(level)
                        level.load_ghost()

            self.pac_affiche = self.font.render('Nombre de vies restantes : '+ str(self.vies), True,  (255, 255, 255))



    def wait(self, seconds):
        self.begin = pygame.time.get_ticks()
        self.end = seconds + seconds






    def venere(self):
        self.mode_venere =  True
        self.last_time = pygame.time.get_ticks()


    def animate(self):
        if self.speed_x !=0 or self.speed_y !=0:
            if self.index <2:
                self.index += parametres.animation_s
            else:
                self.index = 0

            if self.index >=2:
                self.index = 0

            self.image = self.images.get(self.direction)[int(self.index)]

        #self.image = parametres.resize(self.image, parametres.tile_size)
            if self.direction in ['right', 'down']:
                self.rect = self.image.get_rect(topleft= self.rect.topleft)
            elif self.direction == 'up':
                self.rect = self.image.get_rect(bottomleft= self.rect.bottomleft)
            else:
                self.rect = self.image.get_rect(topright= self.rect.topright)


    def determine_pos(self):
        self.x_pos = self.rect.x // parametres.tile_size
        self.y_pos = self.rect.y // parametres.tile_size

        if self.direction == 'up':
            self.y_pos = self.rect.bottom // parametres.tile_size

        elif self.direction == 'left':
            self.x_pos = self.rect.right // parametres.tile_size



        t = parametres.tile_size
        s= pygame.display.get_surface()
        self.x , self.y = self.x_pos, self.y_pos
        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*self.y), (t *(self.x+1), t*self.y        ))

        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*self.y), (t *(self.x), t*(self.y+1)        ))

        pygame.draw.line(s, (255, 0,0) , (t *( self.x+1) , t*self.y), (t *(self.x+1), t*(self.y+1)        ))

        pygame.draw.line(s, (255, 0,0) , (t * self.x , t*(self.y+1)), (t *(self.x+1), t*(self.y +1)       ))


    def where_can_go(self, layout):
        x = self.rect.x // parametres.tile_size
        y = self.rect.y // parametres.tile_size

        rep = []
        #on teste à gauche


        if y < 0 or y >= len(layout):
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





    def is_on_map(self):
        if self.rect.right>= 0 and self.rect.left <= parametres.largeur_ecran:
            if self.rect.bottom >= 0 and self.rect.top <= parametres.hauteur_ecran:
                return True

        return False


    def boucle(self, ecran, level):


        self.old_dirc = self.direction

        murs = level.murs
        
        self.get_input(level)
        self.move(self.direction)

        if not(self.is_on_map()):
            if self.direction == 'down':
                self.rect.bottom = 0

            else:
                self.rect.top = parametres.hauteur_ecran

        self.determine_pos()


        self.colliding, self.mur_co = self.collide(murs)

        if self.colliding:


            self.x_pos = self.old_location[0]
            self.y_pos = self.old_location[1]

            self.rect.x = parametres.tile_size * self.x_pos
            self.rect.y = parametres.tile_size * self.y_pos







        else:
            pass
            self.animate()

        self.pos_affiche = self.font.render('Score : %s' % str(level.score), True, (255,255,255))



        self.collision_fantomes(level)
       
        #self.move(self.direction)
        self.colliding, self.mur_co = self.collide(murs)





        if self.mode_venere == True:
            if pygame.time.get_ticks() - self.last_time >= self.temps_venere * 1000:
                self.mode_venere = False




        ecran.blit(self.pos_affiche, (0,0))

        ecran.blit(self.pac_affiche, (200,0))
        ecran.blit(self.image, self.rect)
        self.save_location()




    def collide(self, murs):
        for mur in murs:
            if self.rect.colliderect(mur.rect):




                return True, mur
        return False, None


