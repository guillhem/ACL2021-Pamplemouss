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
PV_max = 5
duree_splash_degats = 8


liste_lvl = ["niveau_1.txt","niveau_2.txt"]
N = len(liste_lvl)

taille_sprite = 30

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


l = Lab.fich2lab("niveau_1.txt")

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

#texte de super victoire
txt_sup_vic = police_deb.render("Bravo BG, tu as vaincu SKiBidi!!",True,pamplemou,None)
txt_sup_vicrect = txt_vic.get_rect()
txt_sup_vicrect.center = (330,200)

#%% Images

icone = pygame.image.load(chemin+"icone.jpg")
pygame.display.set_icon(icone)

#GG BG
skib = pygame.image.load(chemin+"skib.png")
skib = pygame.transform.scale(skib, (600,305))

skib_rect = skib.get_rect()
skib_rect.center = (330,400)

# importation du logo
pamp = pygame.image.load(chemin+"pamlemousse.jpg")
pamprect = pamp.get_rect()

#icone joueur
joueur = pygame.image.load(chemin+"joueur_ic.png")
joueur = pygame.transform.scale(joueur, (taille_sprite, taille_sprite))
j_rect = joueur.get_rect()

#icone PV
icone_PV1 = pygame.image.load(chemin+"icone_PV.jpg")
icone_PV1 = pygame.transform.scale(icone_PV1, (taille_sprite, taille_sprite))
PV1_rect = icone_PV1.get_rect()
icone_PV2 = pygame.image.load(chemin+"icone_PV.jpg")
icone_PV2 = pygame.transform.scale(icone_PV2, (taille_sprite, taille_sprite))
PV2_rect = icone_PV2.get_rect()
icone_PV3 = pygame.image.load(chemin+"icone_PV.jpg")
icone_PV3 = pygame.transform.scale(icone_PV3, (taille_sprite, taille_sprite))
PV3_rect = icone_PV3.get_rect()
icone_PV4 = pygame.image.load(chemin+"icone_PV.jpg")
icone_PV4 = pygame.transform.scale(icone_PV4, (taille_sprite, taille_sprite))
PV4_rect = icone_PV4.get_rect()
icone_PV5 = pygame.image.load(chemin+"icone_PV.jpg")
icone_PV5 = pygame.transform.scale(icone_PV5, (taille_sprite, taille_sprite))
PV5_rect = icone_PV5.get_rect()

#pop up dégâts
dmg = pygame.image.load(chemin+"juice.png")
dmg = pygame.transform.scale(dmg, (taille_sprite, taille_sprite))
dmg_rect = dmg.get_rect()


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
