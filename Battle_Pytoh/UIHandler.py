"""Ce ficher contient les fonctions relatives a l'UI"""
import time;
import sys;

def clearScreen():
    print('\n'*1000);

def createSymbolMultiple(length,symbol):
    string = "";    
    i = 0;
    while (i<length):
        string += symbol;
        i += 1;
    return string;    

def createBattleStatSquare(fighter,size):
    
    #La banière avec le nom    
    drawed = "|{}|\n".format(fighter.getName());
    
    #Le haut
    drawed += "*";
    drawed += createSymbolMultiple(size,'-');
    drawed += "*\n";    
    
    #Une ligne écart
    drawed += "|";
    drawed += createSymbolMultiple(size,' ');
    drawed += "|\n";
    
    #Ecrire les infos
    drawed += "|";
    tempInfo = "Pv : {}".format(fighter.getPv());
    drawed += tempInfo;
    drawed += createSymbolMultiple(size-len(tempInfo)," ");
    drawed += "|\n";
    
    drawed += "|";
    tempInfo = "Ap : {}".format(fighter.getAttackPoints());
    drawed += tempInfo;
    drawed += createSymbolMultiple(size-len(tempInfo)," ");
    drawed += "|\n";
    
    #Une ligne écart
    drawed += "|";
    drawed += createSymbolMultiple(size,' ');
    drawed += "|\n";
    
    #Le bas
    drawed += "*";
    drawed += createSymbolMultiple(size,'-');
    drawed += "*\n";    
    
    
    return drawed;



def printBattleArena(player,enemy):
    clearScreen();
    
    print(createBattleStatSquare(player,14));
        
    print(createBattleStatSquare(enemy,14));


 
def chooseBattleActions(possibleAction):
   
    print("Actions possibles : ");
    
    i = 0;
    while(i<len(possibleAction)):
        print("[{}]{}".format(i,possibleAction[i]));
        i += 1;

    print("\nQue Faire ?");    
    choosed = -1;
    while(choosed<0 or choosed>len(possibleAction)-1):
        choosed = int(input());
    
    return possibleAction[choosed];    


    
def waitToResume():
    print("Appuyer sur Entrée pour continuer...");
    input();
    
    
def printTextAnimation(textToPrint,delay = 0.05):
    for letter in textToPrint:
        print(letter, end="");
        time.sleep(delay);    

def nextRoundAnimation(roundId,player,enemy,newEnemy,obtainedItem=None):
    
    #Round Suivant
    clearScreen();
    if(roundId > 0):
        printTextAnimation("Félicitation Aventurier {}, vous avez vaincu {} qui s'écroule sur le sol !!\nMais des ennemis plus forts encore vous attendent peut être...".format(player.getName(), enemy.getNameWithDeterminer().lower()));
        printTextAnimation("\n Vous obtenez un(e) {}".format(obtainedItem.getName().lower()));
        sys.stdout.flush();
        time.sleep(1);
    
 
    printTextAnimation("\n\n----====Round {}====----\n".format(roundId));  
    sys.stdout.flush();
    
    #Texte   
    introText = "{} vous barre la route !".format(newEnemy.getNameWithDeterminer());
    printTextAnimation(introText);
    sys.stdout.flush();
    time.sleep(4);
    
    
def introSequence():
    clearScreen();
    #Splash Screen    
    printTextAnimation("""                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((
                *------------------------*
                |   Pytoh Battle v0.1    |
                *------------------------*              
                          
              \n\n\n\n\n\n\n\n\n\n\n\n
    """,0.01);
    print("");
    sys.stdout.flush();
    
    time.sleep(2);
    
def gameOverAnimation(enemy,currentRoundId):
    print("{} vous inflige le coup fatal ! Vous tombez à terre, et fermez les yeux....\nVous êtes mort après {} bataille(s)...".format(enemy.getNameWithDeterminer(),currentRoundId));    
    
 
                                                      
