



#%% importations 

from Lab import *
from param import *
from Monstre2 import *
from TP import *



#%%


class Personnage():
    def __init__(self, labDuPerso, nbVies):
        self.__labDuPerso=labDuPerso.getMatrice()
        self.__position=np.where(self.__labDuPerso==3)[0][0], np.where(self.__labDuPerso==3)[1][0]  #position initiale
        self.__etat=nbVies # nombre de vies
        self.__win=False # = True quand le personnage a atteint la sortie
        
        self.__compteur = 0
        self.__monstres = {}
       
        
        
    def get_etat(self) :
        return(self.__etat)
    def get_win(self) :
        return(self.__win)
    def get_lab(self) :
        return(self.__labDuPerso)
    def get_monstres(self):
        return(self.__monstres)

    def initMonstres(self): # pour initialiser le dico monstres
        n=np.size(self.__labDuPerso[0])    
        for i in range(n):
            for j in range(n):
                if self.__labDuPerso[i,j]==8:
                    self.__monstres[str(i)+" "+str(j)]= Monstre([i,j], self.__labDuPerso,8)
                if self.__labDuPerso[i,j]==9:
                    self.__monstres[str(i)+" "+str(j)]= Monstre([i,j], self.__labDuPerso,9)
            
                    #nom du monstre dans le dico "i j" sa position de départ
                
        
        
        
    def set_changement(self,i,j,new): #non utilisé
        self.__labDuPerso[i][j]=new


    def incrementeCompteur(self):
        self.__compteur+=1

    def checkCompteur(self):
        if self.__compteur%20 == 0:
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
        
        elif self.__labDuPerso[i][j]==6 :  # case PV
            if self.__etat < PV_max :
                self.__etat+=1
            self.__labDuPerso[posi][posj]=0 # le personnage se déplace dans le lab
            self.__labDuPerso[i][j]=3 # potion utilisée
            self.__position=[i,j]
            
        elif self.__labDuPerso[i][j] >6 :
            
            for monstre in self.__monstres.keys() :   # cherche le monstre au niveau du perso
                mi,mj = monstre.split(' ')
                if (mi == str(i) or mj == str(j)) and self.__monstres[monstre].getTouchePerso() == False :
                    self.__etat -= 1




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
    
    def monstreTouche(self): #pour que le monstre fasse perdre une vie au perso si il va sur la case où est le personnage
        for monstre in self.__monstres.values():
            if monstre.getTouchePerso()==True:
                self.__etat-=1
                monstre.reintTouchePerso()
    
    
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
                    screen.blit(pot,(x,y))
                if L[j][i] > 6 :
                    screen.blit(monstr,(x,y))
                
                    
                    
                    
        
    
    def reset(self,niveau) : 
        l = fich2lab(niveau)
        self.__init__(l,PV_max)
        self.__compteur = 0
        self.initMonstres()

            
