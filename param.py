# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 06:12:45 2021

@author: sabri
"""
import pygame
import Lab


pygame.init()

chemin = "images/"

# param perso
PV_max = 3


liste_lvl = ["niveau_1.txt", "niveau_2.txt"]
N = len(liste_lvl)


#  propriétés de la fenêtre
title = "PAMPLEMOUSS"
size = width, height = 660, 690
speed = [1,1]
black = 0, 0, 0
# black_t = 0, 0, 0, 150
fond_c = 153,224,91

pamplemou = 246, 67, 113   #f64371

screen = pygame.display.set_mode(size)
rectScreen = screen.get_rect()

pygame.display.set_caption(title)

taille_sprite = 30

toucheq = ["z","q","s","d"]

touchef = ["k_UP","K_LEFT","K_DOWN","K_RIGHT"]
#%% MUSIQUE
#musique de fond  
pygame.mixer.music.load("KIBI.mp3")
pygame.mixer.music.play(loops=-1) # se répète à l'infini


#%% TEXTES
police_deb = pygame.font.Font("consolas.ttf",35)
police = pygame.font.Font("consolas.ttf",50)
police_ui = pygame.font.Font("consolas.ttf",20)

# texte de début
txt_debut = police_deb.render("Appuyez sur espace",True,pamplemou,black)
txt_debut2 = police_deb.render("pour commencer une partie",True,pamplemou,black)

txt_debutrect = txt_debut.get_rect(center=(330,275))
txt_debutrect2 = txt_debut2.get_rect(center=(330,335))




#texte de mort
txt_mort = police.render("T'es mort dommaj",True,pamplemou,None)
txt_mortrect = txt_mort.get_rect()
txt_mortrect.center = rectScreen.center

#texte de victoire
txt_vic = police.render("Niveau réussi ! GG bg",True,pamplemou,None)
txt_vicrect = txt_vic.get_rect()
txt_vicrect.center = rectScreen.center


#%% Images

icone = pygame.image.load(chemin+"icone.jpg")
pygame.display.set_icon(icone)

# importation du logo
pamp = pygame.image.load(chemin+"pamlemousse.jpg")
pamprect = pamp.get_rect()

#icone joueur
joueur = pygame.image.load(chemin+"joueur_ic.png")
joueur = pygame.transform.scale(joueur, (taille_sprite, taille_sprite))
j_rect = joueur.get_rect()

#NIVEAU

    #fond 
fond = pygame.image.load(chemin+"fond.png")
fond = pygame.transform.scale(fond, size)
f_rect = fond.get_rect()
f_rect.center = rectScreen.center


   # cases
mur = pygame.image.load(chemin+"image_mur.png").convert_alpha()
mur = pygame.transform.scale(mur, (taille_sprite, taille_sprite))

piege = pygame.image.load(chemin+"image_piege.png").convert()
piege = pygame.transform.scale(piege, (taille_sprite, taille_sprite))

monstr = pygame.image.load(chemin+"couteau.png").convert_alpha()
monstr = pygame.transform.scale(monstr, (taille_sprite, taille_sprite))

tp = pygame.image.load(chemin+"image_tp.png").convert()
tp = pygame.transform.scale(tp, (taille_sprite, taille_sprite))

pot = pygame.image.load(chemin+"potion.png").convert_alpha()
pot = pygame.transform.scale(pot, (taille_sprite, taille_sprite))

arrivee = pygame.image.load(chemin+"image_arrivee.png").convert_alpha()
arrivee = pygame.transform.scale(arrivee, (taille_sprite, taille_sprite))


direc = pygame.image.load(chemin+"direction.png").convert_alpha()
direc = pygame.transform.scale(direc, (200, 200))
direc_rect = direc.get_rect()
direc_rect.bottomleft = rectScreen.bottomleft
