"""Ce fichier contient la classe Ennemies"""

from Fighter import *;

class Enemy(Fighter):
    
    
    def __init__(self,determiner,name,pv,attackPoints):
       Fighter.__init__(self,determiner,name,pv,attackPoints);

    def printStat(self):
        print("Le monstre {}".format(Fighter.getStat(self)));
    
    def receiveNewEnemy(self,newEnemy):
        self.__init__(newEnemy.determiner,newEnemy.name,newEnemy.pv,newEnemy.attackPoints);