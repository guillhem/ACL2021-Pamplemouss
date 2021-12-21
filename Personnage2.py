



#%% importations 

from Lab import *
from param import *
from Monstre import *
from TP import *



#%%
nbVies = 1

class Personnage():
    def __init__(self, labDuPerso, nbVies, nbPersonnages=1):
        self.__position=[1,1] # [1,1] case en haut à gauche
        self.__etat=nbVies # nombre de vies
        self.__win=False # = True quand le personnage a atteint la sortie
        self.__labDuPerso=labDuPerso.getMatrice()
        self.__compteur=0
        self.__monstres = {}
        self.__monstres["monstre_1"] = Monstre([5,7], "horiz", periode_deplacement=1)
        
        
        
    def get_etat(self):
        return(self.__etat)
    def get_win(self):
        return(self.__win)

    def get_lab(self):
        return(self.__labDuPerso)

    def set_changement(self,i,j,new): #non utilisé
        self.__labDuPerso[i][j]=new
        
    def incrementeCompteur(self):
        self.__compteur+=1
    
    def checkCompteur(self):
        if self.__compteur//50 ==0:
            for monstre in self.__monstres.values():
                monstre.order()

    def direct(self,i,j,posi,posj) :   #posi, posj position actuelle du héros
        
        if self.__labDuPerso[i][j]==0: # si la case est vide
            self.__labDuPerso[posi][posj]=0 # le personnage se déplace dans le lab
            self.__labDuPerso[i][j]=3
            self.__position=[i,j] # on change son paramètre position
            
        elif self.__labDuPerso[i][j]==2 :
            self.__win=True
            
        elif self.__labDuPerso[i][j]==4 :
            self.__etat-=1
        
        elif self.__labDuPerso[i][j]==7 :  # case PV
            if self.__etat < PV_max :
                self.__etat+=1
                # oui ça sert à rien mais j'aime bien
                self.__labDuPerso[posi][posj]=0 # le personnage se déplace dans le lab
                self.__labDuPerso[i][j]=3 # potion utilisée
                self.__position=[i,j]
            
                
        # elif self.__labDuPerso[i][j]==5:
        #     self.inst_relocate(self.__labDuPerso.getDestination())





    def deplacement(self,direction):

        i,j = self.__position
        
        if direction=="q": # gauche
            self.direct(i,j-1,i,j)
                
                
        if direction=="s": # bas
           self.direct(i+1,j,i,j)
                
                
        if direction=="d": # droite
            self.direct(i,j+1,i,j)
                    
                
        if direction=="z": # haut
            self.direct(i-1,j,i,j)
    
    
    
    
    def verif_case(self, x, y):
        """vérifie le type de case destination lors du déplacement"""
        #à compléter, ou pas

    def inst_relocate(self, new_pos):
        """si besoin de changer instantanément la position du personnage"""
        self.__position = new_pos
    
    
    
    
    def afficherLab(self):
        
        L = self.__labDuPerso
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
                if L[j][i] == 5 :
                    screen.blit(tp,(x,y))
                if L[j][i] == 6 :
                    screen.blit(monstr,(x,y))
                if L[j][i] == 7 :
                    screen.blit(pot,(x,y))
                    
                    
                    
        
    
    def reset(self) : 
        l = fich2lab("niveau_1.txt")
        self.__init__(l,PV_max)
            
