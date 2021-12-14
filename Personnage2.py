



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
        # self.__monstres = {}
        # self.__monstres["monstre_1"] = Monstre([5,7], "horiz", periode_deplacement=1)
        
        
        
    def get_etat(self):
        return(self.__etat)
    def get_win(self):
        return(self.__win)
# =============================================================================
#     def explicationsDeplacement(self):
#         print("Pour vous déplacer, vous allez utiliser les touches q,s,z,d :\n \
#               q pour vous délacer à gauche,\n \
#               d pour vous délacer à droite,\n \
#               s pour vous délacer en bas,\n \
#               z pour vous délacer en haut.")
# =============================================================================

    def deplacement(self,direction):

        i,j = self.__position
        
        if direction=="q": # gauche
            if self.__labDuPerso[i][j-1]==0: # si la case est vide
                self.__labDuPerso[i][j]=0 # le personnage se déplace dans le lab
                self.__labDuPerso[i][j-1]=3
                self.__position=[i,j-1] # on change son paramètre position
                
            elif self.__labDuPerso[i][j-1]==2:
                self.__win=True
                
            elif self.__labDuPerso[i][j-1]==4:
                self.__etat-=1
                
            elif self.__labDuPerso[i][j-1]==5:
                self.inst_relocate(self.__labDuPerso.getDestination())
                
                
        if direction=="s": # bas
            if self.__labDuPerso[i+1][j]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i+1][j]=3
                self.__position=[i+1,j]
                
            elif self.__labDuPerso[i+1][j]==2:
                self.__win=True
                
            elif self.__labDuPerso[i+1][j]==4:
                self.__etat-=1
                
            elif self.__labDuPerso[i+1][j]==5:
                self.inst_relocate(self.__labDuPerso.getDestination())
                
                
                
        if direction=="d": # droite
            if self.__labDuPerso[i][j+1]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i][j+1]=3
                self.__position=[i,j+1]
                
            elif self.__labDuPerso[i][j+1]==2:
                self.__win=True
                
            elif self.__labDuPerso[i][j+1]==4:
                self.__etat-=1
                
            elif self.__labDuPerso[i][j+1]==5:
                self.inst_relocate(name.getDestination())
                    
                
        if direction=="z": # haut
            if self.__labDuPerso[i-1][j]==0:
                self.__labDuPerso[i][j]=0
                self.__labDuPerso[i-1][j]=3
                self.__position=[i-1,j]
                
            elif self.__labDuPerso[i-1][j]==2:
                self.__win=True
                
            elif self.__labDuPerso[i-1][j]==4:
                self.__etat-=1
                
            elif self.__labDuPerso[i-1][j]==5:   # case TP
                self.inst_relocate(self.__labDuPerso.getDestination())     #pk labDuPerso
    
    
    
    
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
                    
                    
                    
        
    
    def reset(self) : 
        l = fich2lab("niveau_1.txt")
        self.__init__(l,1)
        
    
# =============================================================================
#     def play(self):
#         self.explicationsDeplacement()
#         
#         self.afficherLab()
#         
#         while self.etat>0 and self.win==False:
#             self.deplacement()
#             self.afficherLab()
#         
#         if self.win==True:
#             print(" \n Niveau réussi ! GG bg ")
#             
#         if self.etat==0 :
#             print("\n T'es mort dommaj")
#             
#         self.reset()    
#             
# =============================================================================
            
