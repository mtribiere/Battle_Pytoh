"""Ce fichier contient la classe des parchemins derivé de la classe Item"""

from Item import *;

class Scroll(Item):
    def __init__(self,name,effect,actionPoints):
        Item.__init__(self,name);
        self.effect = effect;
        self.actionPoints = actionPoints;
        
    def getEffect(self):
        return self.effect;
    
    def getActionPoints(self):
        return self.actionPoints;
