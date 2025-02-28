# Créé par leonardr, le 29/03/2022 en Python 3.7
import os
import pygame

images = {}

def load(name):
    img = {}
    
    for a, b, files in os.walk("sprites/ghosts"):
        
        for file_name in files:
            if name in file_name:
                
                image = pygame.image.load("sprites/ghosts/%s"  % file_name)
                #image = pygame.transform.scale(image, (33, 33))
                
                i = 0
                for x in range(len(file_name)):
                    if file_name[x] == '_':
                        i = x + 1 
                direction = file_name[i: len(file_name)]
                
                img[direction] = image
                    
    
    return img









