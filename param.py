# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 06:12:45 2021

@author: sabri
"""
import pygame

pygame.init()

chemin = r"C:/Users/sabri/OneDrive/Bureau/ENSEM cours/2A\ACL/projet_pamplemouss\images/"

taille_sprite = 40

#  propriétés de la fenêtre
title = "PAMPLEMOUU"
size = width, height = 880, 880
speed = [1,1]
black = 0, 0, 0
pamplemou = 246, 67, 113

screen = pygame.display.set_mode(size)
rectScreen = screen.get_rect()

pygame.display.set_caption(title)


#%% MUSIQUE
#musique de fond  
pygame.mixer.music.load("KIBI.mp3")
pygame.mixer.music.play(loops=-1) # se répète à l'infini
pygame.mixer.music.set_volume(0.5)

#%% TEXTES
police = pygame.font.Font("consolas.ttf",60)

# texte de début
txt_debut = police.render("Appuyez sur espace",True,pamplemou,black)
txt_debutrect = txt_debut.get_rect()
txt_debutrect.center = rectScreen.center

#texte de mort
txt_mort = police.render("T'es mort dommaj",True,pamplemou,None)
txt_mortrect = txt_mort.get_rect()
txt_mortrect.center = rectScreen.center

#texte de victoire
txt_vic = police.render("Niveau réussi ! GG bg",True,pamplemou,None)
txt_vicrect = txt_vic.get_rect()
txt_vicrect.center = rectScreen.center

#%% Images

icone = pygame.image.load(chemin+"/icone.jpg")
pygame.display.set_icon(icone)

# importation du logo
pamp = pygame.image.load(chemin+"/pamlemousse.jpg")
pamprect = pamp.get_rect()

#icone joueur
joueur = pygame.image.load(chemin+"/joueur_ic.jpg")
joueur = pygame.transform.scale(joueur, (40, 40))
j_rect = joueur.get_rect()

#NIVEAU

    #fond 
fond = pygame.image.load(chemin+"/fond.png")
f_rect = fond.get_rect()
f_rect.center = rectScreen.center

mur = pygame.image.load(chemin+"/image_mur.png").convert()
piege = pygame.image.load(chemin+"/image_piege.png").convert()
arrivee = pygame.image.load(chemin+"/image_arrivee.png").convert_alpha()
