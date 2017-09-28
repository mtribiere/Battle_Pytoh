"""Ce fichier contient la classe Joueur"""

from Fighter import *;

class Player(Fighter):
    
    def __init__(self,determiner,name,pv,attackPoints):
        Fighter.__init__(self,determiner,name,pv,attackPoints);
    
    def printStat(self):
        print("Le Joueur {}".format(Fighter.getStat(self)));
    
