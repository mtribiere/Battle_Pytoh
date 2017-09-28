"""Ce fichier contient la classe du sac a dos"""

from Item import *;
from ItemHolder import *;
from Amulet import *;

class BackPackHolder:
    
    def __init__(self):
        self.items = [];
    
    def getItemList(self):
        listed = "";        
        for item in self.items:
            listed += item.getName;
            listed += "\n";
        return listed;   
        
    def chooseItem(self):     
        print("Objets dans le sac : ");
    
        i = 0;
        while(i<len(self.items)):
            print("[{}]{}".format(i, self.items[i].getName()));
            i += 1;
        print("\n[99]Retour");
          
        choosed = -1;
        while((choosed<0 or choosed>len(self.items)-1) and choosed != 99):
            if(choosed != ""):
                print("\nLequel prendre ?");  
                choosed = int(input());
            else: 
                choosed = -1;
            
        if(choosed == 99): 
            return "Back";
        
        choosedItem = self.items[choosed];

        if(choosedItem.__class__.__name__ == "Amulet"):
            choosedItem.itemUsed();
            if(choosedItem.isUsedMax()):
                self.removeItem(choosed);
        else:
            self.removeItem(choosed);

        return choosedItem;
    
    def storeItem(self,itemToStore):
        self.items.append(itemToStore);
    
    def removeItem(self,id):
        del self.items[id];
        
    def getItemById(self,id):
        return self.items[id];

    def getItemsCount(self):
        return len(self.items);