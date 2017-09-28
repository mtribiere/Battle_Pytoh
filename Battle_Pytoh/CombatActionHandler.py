"""Ce fichier contient les fonctions relatives aux actions et au déroulement des combats"""
from BackPackHolder import *;
from random import randrange;

from Item import *;
from Potion import *;
from Amulet import *;

from Enemy import *;
from MobHolder import *;

from UIHandler import *;

def executeCombatAction(action,player,enemy,backPack):
    #Attaquer
    if(action == "Attaquer"):
        player.attack(enemy);
    
    #Ouvrir le Sac
    if(action == "Ouvrir le sac"):
        clearScreen();
        print("Vous ouvrez le sac...\n")        
        choosedItem = backPack.chooseItem();
        
         ##################################Si c'est une annulation
        if(choosedItem.__class__.__name__ == 'str'):
           return False;
        
         ##################################Si c'est une Potion        
        if(choosedItem.__class__.__name__ == 'Potion'):
             print("Vous utilisez la {}.".format(choosedItem.getName().lower()), end='');
             if(choosedItem.getIsBenefic()):
                    print("Vous gagnez {} points de vies !".format(choosedItem.getActionPoints()));
                    player.pv += choosedItem.getActionPoints();
             else:
                    print("Vous lancez la potion sur {}, qui pert {} points de vies !".format(enemy.getNameWithDeterminer().lower(),choosedItem.getActionPoints()));
                    enemy.pv -= choosedItem.getActionPoints();       


                    
        ##################################Si c'est un parchemin
        if(choosedItem.__class__.__name__ == "Scroll"):
            print("Vous lisez le {}.".format(choosedItem.getName().lower()), end ='');
            
            #Si l'effet est l'aspiration
            if(choosedItem.getEffect() == "Aspire"):
                print("{} sent ses forces s'atténuées, vous lui voler {} de points de vies".format(enemy.getNameWithDeterminer(),choosedItem.getActionPoints()));
                enemy.pv -= 2;
                player.pv += 2;


            #Si l'effet est une compétence aléatoire
            if(choosedItem.getEffect().split(':')[0] == "RandomStatAdd"):
                randomValue = randrange(int(choosedItem.getActionPoints().split(':')[0]),int(choosedItem.getActionPoints().split(':')[1]));      
                affectedStat = choosedItem.getEffect().split(':')[1];                 
        
                #Si l'effet est bénéfique
                if(randomValue > 0):
                    #Si on modifie l'AP
                    if(affectedStat == "AP"):
                        print(" Vous avez de la chance, votre épée gagne {} point(s) d'attaque(s)".format(randomValue));
                        player.attackPoints += randomValue;
                    #Si on modifie les PV    
                    if(affectedStat == "PV"):
                        print("Vous de la chance, le sort vous est favorable, vous gagnez {} point(s) de vie".format(randomValue));
                        player.pv += randomValue;

                #Si l'effet n'est pas bénéfique  
                if(randomValue < 0):
                    #Si on modifie l'AP
                    if(affectedStat == "AP"):
                        print(" Mais pas de chance votre épée pert {} point(s) d'attaque(s)".format(randomValue));
                        player.attackPoints += randomValue;
                    #Si on modifie les PV    
                    if(affectedStat == "PV"):
                        print("Mais pas de chance, vous perdez {} point(s) de vie".format(randomValue));
                        player.pv += randomValue;    
                 
                #Si l'effet est neutre 
                if(randomValue == 0):
                    print(" Mais pas de chance, il ne se passe rien...");
                        

                        
            #Si l'effet est l'enchantement
            if(choosedItem.getEffect() == "Enchantment"):
                print(" Vous sentez votre épée vibrer légérement. Elle gagne {} points d'attaques".format(choosedItem.getActionPoints()));
                player.attackPoints += choosedItem.getActionPoints();
                
            #Si l'effet est le switch de PV
            if(choosedItem.getEffect() == "PVSwitch"):
                print("Les points de vies de votre ennemi(e) et les votres viennent de s'echanger !");
                tempPv = player.getPv();
                player.pv = enemy.getPv();
                enemy.pv = tempPv;

        ##################################Si c'est une amulette
        if(choosedItem.__class__.__name__ == "Amulet"):
            print("Vous utilisez {} qui brille dans le noir. ".format(choosedItem.getName()),end='');

            #Si l'effet est la restauration de PV
            if(choosedItem.getEffect() == "RestorePV"):
                print("Vous recuperez {} point(s) de vie !".format(choosedItem.getActionPoints()));
                player.pv += choosedItem.getActionPoints();
            #Si l'effet est la soustraction de PV
            if(choosedItem.getEffect() == "RemovePV"):
                print("Elle dégage une vague d'énérgie qui blesse {} ! {} pert {} points de vies".format(enemy.getNameWithDeterminer().lower(),enemy.getNameWithDeterminer(),choosedItem.getActionPoints()));
                enemy.pv -= choosedItem.getActionPoints();

            #Si l'effet est le mélange du sac
            if(choosedItem.getEffect() == "ShuffleBackPack"):
                print("Vous sentez votre sac bouger..... Tout vos objects ont été changés !");

                toGenerate = backPack.getItemsCount();
                print(toGenerate);
                i = 0;
                while (i < toGenerate):
                    backPack.removeItem(0);
                    i += 1;
                i = 0;
                while (i < toGenerate):
                    backPack.storeItem(ItemHolder().pickRandomItem());
                    i += 1;

    #Fuir
    if(action == "Fuir"):
        #Pour le debug
        #enemy.getDamage(999);
        
        print("Vous ne pouvez pas fuir !");
     
     
    return True;  
    
def initBattle(player,enemy,backPack):
    #Creer le nouvel ennemis
    newEnemy = MobHolder().pickRandomMob();    
    enemy.receiveNewEnemy(newEnemy);    

    #Mettre en place le sac, et y ajouter deux items aléatoires
    backPack.storeItem(ItemHolder().pickRandomItem());
    backPack.storeItem(ItemHolder().pickRandomItem());
    
    #Lancer l'animation du round
    nextRoundAnimation(0,player,backPack,enemy,newEnemy);

def nextRound(currentRoundId,player,backPack,enemy):
    
    if(currentRoundId > 0):
        obtainedItem = ItemHolder().pickRandomItem();
        backPack.storeItem(obtainedItem);    
    
    newEnemy = MobHolder().pickRandomMob();
    
    nextRoundAnimation(currentRoundId,player,enemy,newEnemy,obtainedItem);        
        
    enemy.receiveNewEnemy(newEnemy);
        

