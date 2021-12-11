



#%% importations 

from Lab import *
from Monstre import *


#%%
nbVies = 1

#TODO: encapsulation

class Personnage():
    def __init__(self, labDuPerso, nbVies, nbPersonnages=1):
        self.__position=[1,1] # [1,1] case en haut à gauche
        self.__etat=nbVies # nombre de vies
        self.__win=False # = True quand le personnage a atteint la sortie
        self.__labDuPerso=labDuPerso.getMatrice()
        self.__monstres=[]
        monstre_1= Monstre([5,7], "horiz", periode_deplacement=1)
        self.__monstres.append(monstre_1)
        #TODO: vérif périodique HF pos_perso==pos_monstre
        
    def explicationsDeplacement(self):
        print("Pour vous déplacer, vous allez utiliser les touches q,s,z,d :\n \
              q pour vous déplacer à gauche,\n \
              d pour vous déplacer à droite,\n \
              s pour vous déplacer en bas,\n \
              z pour vous déplacer en haut.")

        
        
    def deplacement(self):
        print("PV = "+str(self.__etat))
        direction=input("direction de déplacement ? : ")
        i,j = self.__position
        # i=self.position[0]
        # j=self.position[1]
        
        if direction=="q": # gauche
            if self.__labDuPerso[i][j-1]==0: # si la case est vide
                self.__labDuPerso[i][j]=0 # le personnage se déplace dans le lab
                self.__labDuPerso[i][j-1]=3
                self.__position=[i,j-1] # on change son paramètre position
                
            elif self.__labDuPerso[i][j-1]==2:
                self.__win=True
                
            elif self.__labDuPerso[i][j-1]==4:
                self.__etat-=1
                
                
        if direction=="s": # bas
            if self.__labDuPerso[i+1][j]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i+1][j]=3
                self.__position=[i+1,j]
                
            elif self.__labDuPerso[i+1][j]==2:
                self.__win=True
                
            elif self.__labDuPerso[i+1][j]==4:
                self.__etat-=1
                
        if direction=="d": # droite
            if self.__labDuPerso[i][j+1]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i][j+1]=3
                self.__position=[i,j+1]
                
            elif self.__labDuPerso[i][j+1]==2:
                self.__win=True
                
            elif self.__labDuPerso[i][j+1]==4:
                self.__etat-=1
                
        if direction=="z": # haut
            if self.__labDuPerso[i-1][j]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i-1][j]=3
                self.__position=[i-1,j]
                
            elif self.__labDuPerso[i-1][j]==2:
                self.__win=True
                
            elif self.__labDuPerso[i-1][j]==4:
                self.__etat-=1
                
                
    def afficherLab(self):
        print(self.__labDuPerso)
    
    def reset(self) : 
        l=Lab(20)
        l.initLab(tabMursNiveau1)
        
        self.__init__(l,1)
        # self.position=[1,1] # [1,1] case en haut à gauche
        # self.etat=nbVies # nombre de vies
        # self.win=False # = True quand le personnage a atteint la sortie
        # self.labDuPerso=l.matrice
    
    def play(self):
        self.explicationsDeplacement()
        print()
        self.afficherLab()
        
        while self.__etat>0 and self.__win==False:
            self.deplacement()
            self.afficherLab()
        
        if self.__win==True:
            print(" \n Niveau réussi ! GG bg ")
            
        if self.__etat==0 :
            print("\n T'es mort dommaj")
            
        self.reset()    
            
            
#%%

p=Personnage(l,1)
p.play()