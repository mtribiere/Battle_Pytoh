"""Ce fichier contient la classe des amulettes dérivé de la classe Item"""

from Item import *;

class Amulet(Item):
    def __init__(self,name,effect,actionPoints,maxUseTime):
        Item.__init__(self,name);
        self.effect = effect;
        self.actionPoints = actionPoints;
        self.remainingUseTime = maxUseTime;
        self.maxUseTime = maxUseTime;

    def getName(self):
        if(self.maxUseTime == 1):
            return Item.getName(self);

        return Item.getName(self).format(self.remainingUseTime);

    def getEffect(self):
        return self.effect;

    def getActionPoints(self):
        return self.actionPoints;

    def getRemainingUseTime(self):
        return self.remainingUseTime;

    def itemUsed(self):
        self.remainingUseTime -= 1;

    def isUsedMax(self):
        if(self.remainingUseTime == 0):
            return True;
        else:
            return False;

    def getMaxUseTime(self):
        return self.maxUseTime;