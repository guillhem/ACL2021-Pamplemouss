# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:21:15 2021

@author: sabri
"""

import sys, time, pygame as py
from Personnage2 import *
import Personnage2
from continue_jeu import continue_jeu

py.init()



#%%

p = Personnage(l,1)
continuer = 1


while continuer : #boucle principale
    
    continuer_jeu = 1
    continuer_accueil = 1
 #%%   
    #boucle d'écran d'accueil
    while continuer_accueil :
        
        py.mixer.music.set_volume(0.5)
        # py.time.Clock().tick(30)
        
        for event in py.event.get() :
        
            if event.type == py.QUIT : #fermeture du jeu si l'on appuie sur la croix
                continuer_accueil = 0
                continuer_jeu = 0
                
                py.display.quit()
                py.quit()
                sys.exit()
                continuer = 0
                
            if event.type == py.KEYDOWN : 
                touche = py.key.name(event.key)
                if touche == 'space' :
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
        screen.blit(direc,direc_rect)
        time.sleep(0.01)
        py.display.flip() 

            
    # affichage du niveau   
      
    py.mixer.music.set_volume(0.1)
     
    screen.blit(fond,f_rect)
    p.afficherLab()
    py.display.flip()
    
#%%
    # Boucle de jeu

    while continuer_jeu :
        
        py.time.Clock().tick(30)
        
        for event in py.event.get():

            if event.type == py.QUIT :
                py.display.quit()
                py.quit()
                sys.exit()
                continuer_jeu = 0
                continuer = 0
                
            if event.type == py.KEYDOWN :
                
                direction = py.key.name(event.key)
                p.deplacement(direction)
                
                if p.win == True :   #Le joueur est sorti du labyrinthe
                    screen.blit(fond,f_rect)
                    screen.blit(txt_vic,txt_vicrect)
                    py.display.flip() 
                    time.sleep(3)
                    
                    continuer_jeu = 0
                    
                    
                if p.etat == 0 :     #Le joueur meurt
                    screen.blit(fond,f_rect)
                    screen.blit(txt_mort,txt_mortrect)
                    py.display.flip()
                    time.sleep(3)
                    
                    continuer_jeu = 0
                    
                    
            screen.blit(fond,f_rect)
            p.afficherLab()
            time.sleep(0.01)
            py.display.flip()
                    
        
    p.reset()
        
                    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    