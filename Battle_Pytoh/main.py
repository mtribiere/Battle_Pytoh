"""Programme principale du combat"""
#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-

from UIHandler import *;

from MobHolder import *;
from CombatActionHandler import *;

from BackPackHolder import *;
from Item import *;
from Potion import *;
from ItemHolder import *;

from Fighter import *;
from Enemy import *;
from Player import *;

currentRoundId = 0;

player = Player("","Hive",12,5);
enemy = Enemy("","Ghost In the Shell",0,0);
backPack = BackPackHolder();

#Sequence d'introduction
introSequence();

#Initialisation
initBattle(player,enemy,backPack);

while(player.isDead() == False):
    actionValidated = False;
    #Tour du joueur    
    while(actionValidated == False):
        printBattleArena(player,enemy);

        choise = chooseBattleActions(["Attaquer","Ouvrir le sac","Fuir"]);
        actionValidated = executeCombatAction(choise,player,enemy,backPack);
        
    waitToResume();
    
    #Verifier si l'enemi n'est pas mort
    if(enemy.isDead() == False):
        #Tour de l'enemi
        printBattleArena(player,enemy);
        enemy.attack(player);
        waitToResume();
    else:
        currentRoundId += 1;
        nextRound(currentRoundId,player,backPack,enemy);
        
        
gameOverAnimation(enemy,currentRoundId);