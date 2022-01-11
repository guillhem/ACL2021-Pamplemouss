# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:21:15 2021

@author: sabri
"""

import sys, time, pygame as py
from Personnage2 import *
from menu_pause import pause
from Monstre2 import *


py.init()



#%%

p = Personnage(l,PV_max)
p.initMonstres()


continuer = 1


while continuer : #boucle principale
    
    
    continuer_jeu = 1
    continuer_accueil = 1
    mute = 0  #intéret booleen
 #%%   
    #boucle d'écran d'accueil
    if not mute :
        py.mixer.music.set_volume(0.4)

    while continuer_accueil :
        
        
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
                # mute
                if touche == "m" :
                    if mute :
                        py.mixer.music.set_volume(0.4)
                        mute = 0
                    else :
                        py.mixer.music.set_volume(0)
                        mute = 1
                        
                if touche == "space" :
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
        screen.blit(txt_debut2,txt_debutrect2)
       
        
        screen.blit(direc,direc_rect)
        time.sleep(0.01)
        py.display.flip() 

            
    # affichage du niveau 1 et initialisation du jeu
    lvl = 0
    l = fich2lab(liste_lvl[lvl])
    p = Personnage(l,PV_max)
    p.initMonstres()
    
    if not mute :
        py.mixer.music.set_volume(0.2)
     
    screen.blit(fond,f_rect)
    p.afficherLab()
    py.display.flip()
    
#%%
    # Boucle de jeu

    while continuer_jeu :
        
        
        for event in py.event.get():

            if event.type == py.QUIT :
                py.display.quit()
                py.quit()
                sys.exit()
                continuer_jeu = 0
                continuer = 0
                
            if event.type == py.KEYDOWN :
                
                touche = py.key.name(event.key)
                # mute
                if touche == "m" :
                    if mute :
                        py.mixer.music.set_volume(0.1)
                        mute = 0
                    else :
                        py.mixer.music.set_volume(0)
                        mute = 1
                  
                
                # pause
                if touche == "escape" :
                    continuer_jeu, continuer = pause()
                    
                p.deplacement(touche)
                
            if p.get_win() :   #Le joueur est sorti du niveau
                
                if lvl < (N-1) : #on passe au niveau suivant
                    screen.blit(fond,f_rect)
                    screen.blit(txt_vic,txt_vicrect)
                    py.display.flip() 
                    time.sleep(1)  
                    lvl += 1
                    p.reset(liste_lvl[lvl])
                    
                elif lvl == N-1 :   #dernier lvl
                    
                    screen.blit(fond,f_rect)
                    screen.blit(txt_sup_vic,txt_sup_vicrect)
                    screen.blit(skib,skib_rect)
                    py.display.flip() 
                    time.sleep(1)  
                    
                    continuer_jeu = 0 #LE JOUEUR A FINI TOUS LES NIVEAUX
                    # lvl = 0
            
            
            
            if p.get_etat() <= 0 :     #Le joueur meurt
                screen.blit(fond,f_rect)   #changer en screen.fill partout?
                screen.blit(txt_mort,txt_mortrect)
                py.display.flip()
                time.sleep(1)
                if lvl < N :  #on recommence le niveau
                    p.reset(liste_lvl[lvl])
            
            
        #txt ui      
        ui = police_ui.render("PV :",True,pamplemou,None)
        PV1_rect.bottomleft = (50, 690)
        PV2_rect.bottomleft = (60, 690)
        PV3_rect.bottomleft = (70, 690)
        PV4_rect.bottomleft = (80, 690)
        PV5_rect.bottomleft = (90, 690)
        
        
        ui = police_ui.render("PV = "+str(p.get_etat()),True,pamplemou,None) 
        m = police_ui.render("Niveau "+str(lvl+1)+"       Pause : ECHAP   Mute : M",True,pamplemou,None)
        m = police_ui.render("Pause : ECHAP     Mute : M",True,pamplemou,None)
        ui_rect = ui.get_rect()
        ui_rect.bottomleft = (5,685)
        m_rect = m.get_rect()
        m_rect.bottomright = (600,685)
        
        #rafraichit lab
        screen.fill(fond_c)
        # screen.blit(fond,f_rect) #changer en screen.fill partout
        screen.blit(ui,ui_rect)
        screen.blit(m,m_rect)
        
        #affichage coeurs barre de vie
        Coeurs_PV=[
                    [icone_PV1, PV1_rect],
                    [icone_PV2, PV2_rect],
                    [icone_PV3, PV3_rect],
                    [icone_PV4, PV4_rect],
                    [icone_PV5, PV5_rect]
                   ]
        for i in range(p.get_etat()):
            screen.blit(Coeurs_PV[i][0], Coeurs_PV[i][1])
        
        p.incrementeCompteur() # pour les monstres
        p.checkCompteur()
        p.monstreTouche()
        
        p.afficherLab()
        time.sleep(0.01)

        py.display.flip()
                    
        
    p.reset(liste_lvl[lvl])
        
                    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
