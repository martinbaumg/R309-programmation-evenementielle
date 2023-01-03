# R309-programmation-evenementielle
 
### Dans ce repository, vous trouverez les différentes parties du cours : 
- [Thread](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Thread)
- [Exception](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Exception)
- [Interface graphique](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Interface-graphique)
- [Socket](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Socket)
### Et surtout l'examen final : 
- [Examen](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Examen)

## Mais aussi, la [SAE 302 - Développer une application communicante.](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/SAE302-application-communicante)

### Introduction
Plusieurs paquets sont requis pour le bon fonctionnement de l'application. Il s'agit de : 
- PyQt5
- psutil
- netaddr
- netifaces
- socket

Pour tous les installer en un coup, je vous propose un script d'installation. Pour lancer le script, il vous suffit d'éxecuter la commande suivante :
```bash 
python3 gui.py
```
Et de faire le choix 1. 


### Fonctionnement
Premièrement, demarrez le serveur avec la commande suivante :
```bash
python3 serveur.py
```

Au lancement du serveur, une adresse IP et un port vous sera demandé, rentrez alors l'adresse IP que vous souhaitez ainsi que le port voulu. Sinon, vous pouvez laisser les valeurs par défaut en appuyant sur **ENTER**, qui sont :
- Adresse IP : 127.0.0.1
- Port : 10000

Une fois le serveur lancé, et une adresse IP et un port attribué vous pouvez démarrer la partie cliente avec la commande suivante :
```bash
python3 gui.py
```

Une fois, les paquets installés, vous pourrez lancer l'application. Vous aurez alors une fenêtre comme celle-ci :

![alt text](https://github.com/martinbaumg/R309-programmation-evenementielle/blob/main/SAE302-application-communicante/img/img1.png)

Il faudra venir ensuite rentrer dans la partie concerner l'adresse IP et le port que vous avez défini sur le serveur. Une fois connecté, un message de connexion apparaîtra et vous pourrez commencer à utiliser le programme.

Le programme a été testé sur une machine MacOS Ventura et debian 11 avec python3 installé par défaut et par l'installation de tous les paquets à l'aide du script présent dans **gui.py** avec le choix **1** au démarrage.
