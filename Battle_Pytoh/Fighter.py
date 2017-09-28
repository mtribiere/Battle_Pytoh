"""Ce fichier contient la classes Combattant"""

class Fighter:
    
    def __init__(self,determiner,name,pv,attackPoints):
        self.determiner=determiner;
        self.name=name;
        self.pv=pv;
        self.attackPoints=attackPoints;
    
    def getDamage(self,damage):
        self.pv -= damage;
        if self.pv <0:
            self.pv=0;
            
    def attack(self,victim):
        print("{} attaque {} ({} points de degat(s))".format(self.getNameWithDeterminer(),victim.getNameWithDeterminer(),self.getAttackPoints()));
        victim.getDamage(self.attackPoints)
        
        
    def modifyStat(self,name,value):
        if(name == "PV"):
            self.pv += value;
            
        if(name == "AP"):
            self.pv += value;
                
    def getName(self):
        return self.name;
        
    def getDeterminer(self):
        return self.determiner;
     
    def getNameWithDeterminer(self):
        return (self.getDeterminer()+" "+self.getName());    
           
    def getPv(self):
        return self.pv;    
        
    def getAttackPoints(self):
        return self.attackPoints;
    
    def getStat(self):
       return ("{} possède actuellement {} points de vies, et attaque avec une force de {} points".format(self.getName(),self.getPv(),self.getAttackPoints()));
    
    def isDead(self):
        if(self.pv<=0):
            return True;
        return False;