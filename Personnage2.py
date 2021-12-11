



#%% importations 

from Lab import *
import pygame
from param import *



#%%
nbVies = 1

class Personnage():
    def __init__(self, labDuPerso, nbVies, nbPersonnages=1):
        self.position=[1,1] # [1,1] case en haut à gauche
        self.etat=nbVies # nombre de vies
        self.win=False # = True quand le personnage a atteint la sortie
        self.labDuPerso=labDuPerso.matrice
        
    def explicationsDeplacement(self):
        print("Pour vous déplacer, vous allez utiliser les touches q,s,z,d :\n \
              q pour vous délacer à gauche,\n \
              d pour vous délacer à droite,\n \
              s pour vous délacer en bas,\n \
              z pour vous délacer en haut.")

        
        
    def deplacement(self,direction):
        
        i,j = self.position
        
        if direction=="q": # gauche
            if self.labDuPerso[i][j-1]==0: # si la case est vide
                self.labDuPerso[i][j]=0 # le personnage se déplace dans le lab
                self.labDuPerso[i][j-1]=3
                self.position=[i,j-1] # on change son paramètre position
                
            elif self.labDuPerso[i][j-1]==2:
                self.win=True
                
            elif self.labDuPerso[i][j-1]==4:
                self.etat-=1
                
                
        if direction=="s": # bas
            if self.labDuPerso[i+1][j]==0:
                self.labDuPerso[i][j]=0
                self.labDuPerso[i+1][j]=3
                self.position=[i+1,j]
                
            elif self.labDuPerso[i+1][j]==2:
                self.win=True
                
            elif self.labDuPerso[i+1][j]==4:
                self.etat-=1
                
        if direction=="d": # droite
            if self.labDuPerso[i][j+1]==0:
                self.labDuPerso[i][j]=0
                self.labDuPerso[i][j+1]=3
                self.position=[i,j+1]
                
            elif self.labDuPerso[i][j+1]==2:
                self.win=True
                
            elif self.labDuPerso[i][j+1]==4:
                self.etat-=1
                
        if direction=="z": # haut
            if self.labDuPerso[i-1][j]==0:
                self.labDuPerso[i][j]=0
                self.labDuPerso[i-1][j]=3
                self.position=[i-1,j]
                
            elif self.labDuPerso[i-1][j]==2:
                self.win=True
                
            elif self.labDuPerso[i-1][j]==4:
                self.etat-=1
                
                
    def afficherLab(self):
        taille_sprite = 40
        L = self.labDuPerso
        n = len(L)
        for i in range (n) :
            for j in range (n) :
                
                x = i*taille_sprite
                y = j*taille_sprite
                
                if L[j][i] == 1 :
                    screen.blit(mur,(x,y))
                if L[j][i] == 4 :
                    screen.blit(piege,(x,y))
                if L[j][i] == 2 :
                    screen.blit(arrivee,(x,y))
                if L[j][i] == 3 :
                    screen.blit(joueur,(x,y))
                    
                    
                    
        
    
    def reset(self) : 
        l=Lab(20)
        l.initLab(tabMursNiveau1)
        
        self.__init__(l,1)
       
