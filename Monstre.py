import time
import random

class Monstre():
    def __init__(self, pos_init, labDuPerso, sens_depl="vert", periode_deplacement=1):
        #self.__pos= [1,2]   #initialisation de la position
        self.__pos= pos_init    #nouvelle position initiale
        self.__sens_depl= sens_depl     #vert ou horiz
        self.__per_depl= periode_deplacement    #période de déplacement du monstre en s
        self.__dead= False
    
        self.__lab = labDuPerso
        #mise en place déplacement périodique monstre
 

    def order(self):
        dir_depl = random.randint(1, 2)
        new_pos = self.__pos
        
        pos0=self.__pos[0]
        pos1=self.__pos[1]
        
        if self.__sens_depl=="vert":
            if dir_depl==1: #haut
                new_pos= [pos0+1, pos1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=6
                    
            elif dir_depl==2: #bas
                new_pos= [pos0-1, pos1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=6
                    
        elif self.__sens_depl=="horiz":
            if dir_depl==1: #gauche
                new_pos= [pos0, pos1-1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=6
                    
            elif dir_depl==2: #droite
                new_pos= [pos0, pos1+1]
                if self.__lab[new_pos[0]][new_pos[1]] == 0:
                    self.__lab[pos0][pos1]=0
                    self.__pos = new_pos
                    self.__lab[new_pos[0],new_pos[1]]=6
                   

    def kill(self):
        """mort du monstre"""
        self.__dead=True    #arrêt depl monstre

    def getPos(self):
        return(self.__pos)
