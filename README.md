<h1>Battle_Pytoh</h1>

## Description
Battle_Pytoh est un un petit jeu de combat écrit en python3. Dans celui-ci vous incarnez le brave aventurier Hive, qui se bat contre un maximum d'ennemis. 

## Systeme de jeu
Chaque personnages, que soit les ennemis ou Hive possedent leurs propres statistiques :<br><br>
Les PV (ou points de vies) qui designent les point de vies. S'ils tombent a 0 c'est la mort du personnage.<br>
Les AP (ou points d'attaques) qui designent les points d'attaques. C'est la force avec laquelle un personnage va pouvoir frapper<br><br>
Les combats s'enchainent jusqu'a votre mort ! Mais heureusement Hive est malin, et a emporté un sac avec lui ! Il a donc sur lui 2 Items alétoires à chaque début de partie, et un Item aléatoire par ennemi vaincu. De plus certains Item ne peuvent étres utiliser qu'un nombre de fois fixe. On utilise alors les UT (point d'utilisation) qui montront combien de fois l'Item peut encore être utiliser 

## Le Bestiaire
Vous pourrez rencontrer dans ce jeu : 

|Ennemis						|PV      |AP      |
|-------------------|:------:|:------:|
|Des Araignées			|10      |3       |    
|Des zombies				|15      |1       |
|Des chauves-souris |6       |5       |
|Des rats           |3       |1       |
|Des fantomes       |18      |4       |
|Des scorpions      |11      |5       |
|Des serpents       |12      |5       |
|Des squelettes     |7       |7       |
|Des dragons        |23      |7       |

##
Les Items
Il existe beaucoup d'items avec chaqun des spécificitées, mais voici quelques exemples avec leur catégorie :<br>

|Categories         |Nom         |Effet    |
|-------------------|:----------:|:-------:|
|Potion|Potion de vie +2|Une potion de vie qui une fois bu donne 2 PV|
|Potion|Poison -2|Une potion de poison qui fait perdre 2 PV a l'adversaire|
|Parchemin|Parchemin d'enchentament d'armes (-3;+1)|Un parchemin magique qui enchante votre arme. Ajoutant aléatoirement une valeur entre -3 et 1 à vos AP|
|Parchemin|Parchemin d'enchantement d'armes +1|Un parchemin magique qui enchante votre arme. Ajoute 1 a vos AP|
|Amulette|Amullette de régéneration +2 (3 UT)|Une amulette aque vous pouvez utilisze 3  fois. Elle redonne 2 PV par utilisation|
|Amulette|Amulette de transformation de sac (1 UT)|Une amulette qui change tout vos items avec d'autres aléatoires !|
