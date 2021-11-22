# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:21:15 2021

@author: sabri
"""

import sys, time, pygame
# from Lab import *
from Personnage2 import *


pygame.init()






#%%

p=Personnage(l,1)
continuer = 1

while continuer : #boucle principale
    
    
    
    continuer_jeu = 1
    continuer_accueil = 1
    
    #boucle d'écran d'accueil
    while continuer_accueil :
        
        # pygame.time.Clock().tick(30)
        
        for event in pygame.event.get() :
        
            if event.type == pygame.QUIT : #fermeture du jeu si l'on appuie sur la croix
                continuer_accueil = 0
                continuer_jeu = 0
                
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                continuer = 0
                
            if event.type == pygame.KEYDOWN : 
                if pygame.key.name(event.key) == 'space' :
                    continuer_accueil = 0
                    
        # animation du logo
        pamprect = pamprect.move(speed)
        if pamprect.left < 0 or pamprect.right > width:
            speed[0] = -speed[0]
        if pamprect.top < 0 or pamprect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(pamp, pamprect)
        screen.blit(txt_debut,txt_debutrect)
        time.sleep(0.01)
        pygame.display.flip() 

            
    # affichage du niveau   
      
    pygame.mixer.music.set_volume(0.1)
     
    screen.blit(fond,f_rect)
    p.afficherLab()
    pygame.display.flip()

    # Boucle de jeu
    while continuer_jeu :
        
        pygame.time.Clock().tick(30)
        
        for event in pygame.event.get():
		
            if event.type == pygame.QUIT :
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                continuer_jeu = 0
                continuer = 0
                
            if event.type == pygame.KEYDOWN :
                
                direction = pygame.key.name(event.key)
                p.deplacement(direction)
                
                if p.win == True :
                    screen.blit(fond,f_rect)
                    screen.blit(txt_vic,txt_vicrect)
                    pygame.display.flip() 
                    time.sleep(3)
                    
                    continuer_jeu = 0
                    
                    
                    
                if p.etat == 0 :
                    screen.blit(fond,f_rect)
                    screen.blit(txt_mort,txt_mortrect)
                    pygame.display.flip()
                    time.sleep(3)
                    
                    continuer_jeu = 0
                    
                    
                    
                
        
        #Affichage nouvelles positions
        
        screen.blit(fond,f_rect)
        p.afficherLab()
        time.sleep(0.01)
        pygame.display.flip()
        
    p.reset()
        
                    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    