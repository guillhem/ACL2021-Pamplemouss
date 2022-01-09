import time
import random

class Monstre():
    def __init__(self, pos_init, labDuPerso,typee):
        
        #typee, type : le type du monstre
        
        # 6 : déplacement aléatoire sur la map
        # 8 : déplacement verticale
        # 9 : déplacement horizontale
        
        
        self.__type=typee 
        self.__pos= pos_init    #nouvelle position initiale
        self.__touchePersonnage= False #quand le monstre touche le personnage,
        # la variable se met à True
        self.__dead= False
    
        self.__lab = labDuPerso
        #mise en place déplacement périodique monstre
 

    def order(self):
        
        dir_depl = random.randint(1, 2)
        new_pos = self.__pos
        
        pos0=self.__pos[0]
        pos1=self.__pos[1]
        
        
        if self.__type==8: # monstre "vertical"
            
            if dir_depl==1: #haut
                new_pos= [pos0+1, pos1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0 :
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=self.__type
                    
                elif self.__lab[new_pos[0]][new_pos[1]] == 3 :
                    self.__touchePersonnage=True
                    
            elif dir_depl==2: #bas
                new_pos= [pos0-1, pos1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=self.__type
                    
                elif self.__lab[new_pos[0]][new_pos[1]] == 3 :
                     self.__touchePersonnage=True
                    
        elif self.__type==9: # monstre "hoizontal"
            if dir_depl==1: #gauche
                new_pos= [pos0, pos1-1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=self.__type

                elif self.__lab[new_pos[0]][new_pos[1]] == 3 :
                     self.__touchePersonnage=True                
                
                    
            elif dir_depl==2: #droite
                new_pos= [pos0, pos1+1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=self.__type
                   
                elif self.__lab[new_pos[0]][new_pos[1]] == 3 :
                     self.__touchePersonnage=True

    
    def getTouchePerso(self):
        return self.__touchePersonnage
    
    def reintTouchePerso(self):
        self.__touchePersonnage=False

    def kill(self):
        """mort du monstre"""
        self.__dead=True    #arrêt depl monstre

    def getPos(self):
        return(self.__pos)

