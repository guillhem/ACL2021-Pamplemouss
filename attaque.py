import Monstre2 as m


class Attaque():
    def __init__(self,p):
        self.__position=p.get_position()
        self.__avant_attaque1=0
        self.__avant_attaque2=0


    def debut_attaque(self, direction,p):
        self.__position=p.get_position()

        i,j = self.__position

        if direction=="e": # touche de l'attaque
            if p.get_lab()[i][j+1]==0:
                    self.__avant_attaque=p.get_lab()[i][j+1]
                    p.get_lab()[i][j+1]=5

    def mouvement_attaque(self,p):
        self.__position=p.get_position()
        for i in range(len(p.get_lab())):
            for j in range(i):
                print(0)
                if p.get_lab()[i][j]==5:
                    if p.get_lab()[i][j+1]==1:
                        p.get_lab()[i][j]=0
                    elif p.get_lab()[i][j+1] in [7,8,9]:
                        p.get_lab()[i][j+1]=0
                        p.get_lab()[i][j]=0

                    else :
                        self._avant__attaque2=p.get_lab()[i][j+1]
                        p.get_lab()[i][j+1]=5
                        p.get_lab()[i][j]=self.__avant_attaque1
                        self._avant__attaque1=self.__avant_attaque2







