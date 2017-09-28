"""Ce fichier contient la classe des potions dérivée de la classe Item"""

from Item import *;

class Potion(Item):
    
    def __init__(self, name, isBenefic, actionPoints):
        Item.__init__(self,name);
        self.isBenefic = isBenefic;
        self.actionPoints = actionPoints;
    
    def getActionPoints(self):
        return self.actionPoints;
     
    def getIsBenefic(self):
         return self.isBenefic;
    

