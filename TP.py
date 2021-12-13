"classe des cases de téléportation"

class TP():
    def __init__(self, destination=[1,1]):
        self.__dest= destination

    def getDestination(self):
        return(self.__dest)