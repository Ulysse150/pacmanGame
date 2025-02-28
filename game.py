import pygame
import parametres
from pacman import Pacman
from level import Level
from ghost import Ghost as G
import time
class Game:

    def __init__(self):

        self.en_cours = True
        self.ecran = pygame.display.set_mode((parametres.largeur_ecran, parametres.hauteur_ecran))

        self.pac_man = Pacman(1, 1)
        self.level = Level()
        self.clock = pygame.time.Clock()
        self.t =  pygame.time.get_ticks()

        self.you_died = pygame.image.load('sprites/mort.png')
        self.you_died = pygame.transform.scale(self.you_died, (777, 703))

        self.police = pygame.font.SysFont("comicsansms", 60)
        self.num_stage = 1


    def main(self):
        self.ecran.fill((0,0,0))
        self.clock.tick(150)
        keys = pygame.key.get_pressed()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.en_cours = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.en_cours = False
                    pygame.quit()

                elif event.key == pygame.K_r:
                    self.restart()

                elif event.key == pygame.K_SPACE:
                    print(pygame.mouse.get_pos())




        if self.pac_man.vies >0:

            self.level.boucle(self.pac_man)
            self.pac_man.boucle(self.ecran, self.level)

            if self.level.gommes == []:
                self.num_stage +=1
                self.you_won = self.police.render('Niveau %s : '% self.num_stage, True, parametres.bleu, (255,255,255))
                self.ecran.blit(self.you_won, (300, 300))
                pygame.display.flip()
                time.sleep(1.5)
                self.restart()



        else:
            self.ecran.blit(self.you_died, (0,0))
            sc = self.police.render(str(self.level.score ) + '.', True, parametres.red)
            self.ecran.blit(sc, parametres.pos_texte)


        pygame.display.flip()


    def restart(self):
        self.pac_man = Pacman(1, 1)
        self.level = Level()


