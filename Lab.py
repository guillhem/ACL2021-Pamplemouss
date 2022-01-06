

# le labyrinthe
# par Guilhem et Sarah

# 0 pour les cases vides
# 1 pour les murs
# 2 pour la sortie
# 3 pour la position du joueur
# 4 pour les pieges
# 5 pour les cases de téléportation
# 6 pour les potions
# 7,8,9 pour les monstres


# on partirait sur des lab de 30x30




#%% importations de bibliothèques 

import numpy as np

from TP import *


#%%


class Lab():
    def __init__(self,n):
        self.__n=n # taille du labyrinthe : nxn
        self.__matrice=np.zeros((n+2,n+2),dtype=int)
              # pour ajouter les murs autour pour faciliter le codage
                    
    def getMatrice(self):
        return(self.__matrice)
    
    def mod_mat(self,mat) :
        self.__matrice = mat
        return None
        
# =============================================================================
#     def initLab(self, tabMurs):
#         
#         
#         # on place des murs autour du labyrinthe
#         # pour faciliter le codage :
#         # pas besoin de vérifier si là où on veut se déplacer est dans la 
#         # matrice, juste si là où on veut se déplacer il y a un mur 
#         
#         for j in range(self.__n+2):
#             self.__matrice[0][j]=1    #mur du haut
#         for j in range(self.__n+2):
#             self.__matrice[-1][j]=1   #mur du bas
#         for j in range(self.__n+2):
#             self.__matrice[j][0]=1    #mur de gauche
#         for j in range(self.__n+2):
#             self.__matrice[j][-1]=1   #mur de droite
#         
#         # placement des murs intérieur
#         for i in range(self.__n):
#             for j in range(self.__n):
#                 self.matrice[i+1][j+1]=tabMurs[i][j]
#             
#         # placement du personnage
#         self.matrice[1][1]=3   #en haut à gauche
#         
#         # placement de la sortie
#         self.matrice[self.n][self.n]=2  #en bas à  droite
#         
#         
#             
#     def ajouterMur(self,i,j): # premiere case où on peut ajouter un mur : 1x1 
#         self.matrice[i][j]=1
#         
#     def enleverMur(self,i,j):
#         self.matrice[i][j]=0
# =============================================================================
        
#%%

def fich2lab(nomfich) :   #Par Sabrina
    with open (nomfich,"r") as nv :
        txt = nv.readlines()
        lab = Lab(len(txt))
        
        # on crée une matrice en concatenat les ligne du txt 
        # et on l'attribue au lab
        m = np.zeros((1,22))
        
        for line in txt :
            line = line.strip()
            mat = [[int(k) for k in line]]
            m = np.concatenate((m,mat))
            
        lab.mod_mat(m[1::])
    
    nv.close()
    return lab
