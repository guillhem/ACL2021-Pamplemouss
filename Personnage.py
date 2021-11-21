



#%% importations 

from Lab import *


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

        
        
    def deplacement(self):
        print("PV = "+str(self.etat))
        direction=input("direction de déplacement ? : ")
        i,j = self.position
        # i=self.position[0]
        # j=self.position[1]
        
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
        print(self.labDuPerso)
    
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
        
        while self.etat>0 and self.win==False:
            self.deplacement()
            self.afficherLab()
        
        if self.win==True:
            print(" \n Niveau réussi ! GG bg ")
            
        if self.etat==0 :
            print("\n T'es mort dommaj")
            
        self.reset()    
            
            
#%%

p=Personnage(l,1)
p.play()