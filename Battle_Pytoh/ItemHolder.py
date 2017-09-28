"""Ce fichier contient la classe relative aux items"""

from Item import *;
from Potion import *;
from Scroll import *;
from Amulet import *;

from random import randrange;

class ItemHolder:
    def __init__(self):
        self.items = [];
        
        self.items.append(Potion("Potion de vie +2",True,2));
        self.items.append(Potion("Potion de vie +5",True,5));
        self.items.append(Potion("Potion d'acide léger -1",False,1));
        self.items.append(Potion("Potion d'acide fort -3",False,3));
        self.items.append(Potion("Poison -2",False,2));
        self.items.append(Potion("Poison -5",False,5));


        self.items.append(Scroll("Parchemin d'aspiration de vie +2","Aspire",2));
        self.items.append(Scroll("Parchemin d'aspiration de vie +3","Aspire",3));
        self.items.append(Scroll("Parchemin d'aspiration de vie +4","Aspire",4));

        self.items.append(Scroll("Parchemin d'enchantement d'armes (-1,+1)", "RandomStatAdd:AP","-1:1"));
        self.items.append(Scroll("Parchemin d'enchantement d'armes (-3,+1)", "RandomStatAdd:AP","-3:1"));
        self.items.append(Scroll("Parchemin d'enchantement d'armes (-1,+3)", "RandomStatAdd:AP","-1:3"));
        self.items.append(Scroll("Parchemin de vie aléatoire (-1;+1)","RandomStatAdd:PV","-1:1"));
        self.items.append(Scroll("Parchemin de vie aléatoire (-3;+1)","RandomStatAdd:PV","-3:1"));
        self.items.append(Scroll("Parchemin de vie aléatoire (-1;+3)","RandomStatAdd:PV","-1:3"));
        self.items.append(Scroll("Parchemin d'enchantement d'armes (-4;4)","RandomStatAdd:AP","-4:4"));

        self.items.append(Scroll("Parchemin d'enchantement d'armes +1","Enchantment",1));
        self.items.append(Scroll("Parchemin d'enchantement d'armes +2","Enchantment",2));
        
        self.items.append(Scroll("Parchemin d'echange de vie","PVSwitch","1"));

        self.items.append(Amulet("Amulette de régénaration +2 ({} UT)","RestorePV",2,3));#3 UT
        self.items.append(Amulet("Amulette de régénaration +3 ({} UT)","RestorePV", 3, 2));#2 UT
        self.items.append(Amulet("Amulette de feu -3 ({} UT)","RemovePV",3,2));#2 UT
        self.items.append(Amulet("Amulette de transformation du sac","ShuffleBackPack",1,1));



    def getItemById(self,id):
        return self.items[id];

    def pickRandomItem(self):
        return self.items[randrange(0,len(self.items)-1)]; 
             