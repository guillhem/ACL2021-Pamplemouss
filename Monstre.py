import asyncio
import random

from Lab import *

class Monstre():
    def __init__(self, pos_init, sens_depl="vert", periode_deplacement=1):
        self.__pos= [1,2]   #initialisation de la position
        self.__pos= pos_init    #nouvelle position initiale
        self.__sens_depl= sens_depl     #vert ou horiz
        self.__per_depl= periode_deplacement    #période de déplacement du monstre en s
        #mise en place déplacement périodique monstre
        self.__loop = asyncio.get_event_loop()
        self.__loop.call_later(5, lambda: self.__task.cancel())
        self.__task = self.__loop.create_task(self.order)
        #démarrage déplacement monstre
        try:
            self.__loop.run_until_complete(self.__task)
        except asyncio.CancelledError:
            pass

    async def order(self):
        while True:
            dir_depl = random.randint(1, 2)
            new_pos = self.__pos
            if self.__sens_depl=="vert":
                if dir_depl==1: #haut
                    new_pos= [self.__pos[0]+1, self.__pos[1]]
                    if not tabMursNiveau1[new_pos[0]][new_pos[1]] == 1:
                        self.__pos = new_pos
                elif dir_depl==2: #bas
                    new_pos= [self.__pos[0]-1, self.__pos[1]]
                    if not tabMursNiveau1[new_pos[0]][new_pos[1]] == 1:
                        self.__pos = new_pos
            elif self.__sens_depl=="horiz":
                if dir_depl==1: #gauche
                    new_pos= [self.__pos[0], self.__pos[1]-1]
                    if not tabMursNiveau1[new_pos[0]][new_pos[1]] == 1:
                        self.__pos = new_pos
                elif dir_depl==2: #droite
                    new_pos= [self.__pos[0], self.__pos[1]+1]
                    if not tabMursNiveau1[new_pos[0]][new_pos[1]] == 1:
                        self.__pos = new_pos
            await asyncio.sleep(self.__per_depl)
    
    def kill(self):
        """mort du monstre"""
        self.__task.cancel()    #arrêt depl monstre

    def getPos(self):
        return(self.__pos)