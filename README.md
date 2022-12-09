# R309-programmation-evenementielle
 
### Dans ce repository, vous trouverez les différentes parties du cours : 
- [Thread](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Thread)
- [Exception]()
- [Interface graphique](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Interface-graphique)
- [Socket](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/Socket)

## Mais aussi, la [SAE 302 - Développer une application communicante.](https://github.com/martinbaumg/R309-programmation-evenementielle/tree/main/SAE302-application-communicante)
### Introduction

J'ai utilisé la version 6 de PyQt, car la version 5 ne fonctionnait pas sur ma machine. Une fois ces paquets fait. Vous pourrez lancer le script **serveur.py**, puis **gui.py**.
Pour lancer les scripts, je faisais au début :
```bash
python3 serveur.py
```
Mais j'avais des erreurs, PyQt6 n'était pas reconnu, alors j'ai changé d'intérpreteur, et j'ai utilisé **python3.11** en faisant donc : 
```bash
python3.11 serveur.py
```
Et ça a fonctionné. Alors je vous suggère de changer d'intérpreteur pour lancer les scripts, si vous avez des erreurs.
### Fonctionnement
Au lancement du serveur, une adresse IP et un port vous sera demandé, rentrez alors l'adresse IP que vous souhaitez ainsi que le port voulu. Sinon, vous pouvez laisser les valeurs par défaut en appuyant sur **ENTER**, qui sont :
- Adresse IP : 127.0.0.1
- Port : 10000

Une fois le serveur lancé, et une adresse IP et un port attribué vous pouvez démarrer la partie cliente avec la commande suivante :
```bash
python3.11 gui.py
```

- Au lancement du script python **gui.py**, vous pourrez choisir d'installer, ou non, les paquets nécessaire au bon fonctionnement de l'application.
Si vous voulez ignorer le téléchargement, appuyez sur n'importe quelle touche au démarrage. Pour information, les paquets requis au bon fonctionnement du programme sont : 

- PyQt6
- psutil
- netaddr
- netifaces

Une fois, les paquets installés, vous pourrez lancer l'application. Vous aurez alors une fenêtre comme celle-ci :

![alt text](https://github.com/martinbaumg/R309-programmation-evenementielle/blob/main/SAE302-application-communicante/img/img1.png)

Il faudra venir ensuite rentrer dans la partie concerner l'adresse IP et le port que vous avez défini sur le serveur. Une fois connecté, un message de connexion apparaîtra et vous pourrez commencer à utiliser le programme.
