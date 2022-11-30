import threading
import os
import platform
import sys


# une fenêtre qui permet de se connecter à un serveur socket et qui propose plusieurs boutons qui permettent d'envoyer des messages au serveur et qui affichent le résultat de la commande envoyée

choix = input("Appuyez sur 1 pour installer les paquets requis, appuyez sur nimporte quelle touche pour continuer : ")

if choix == "1":
    os.system("pip3 install psutil")
    os.system("pip install psutil")
    os.system("python3.11 -m pip install psutil")
    os.system("python3 -m pip install psutil")
    os.system("python3 -m pip install PyQt6")
    os.system("python3.11 -m pip install PyQt6")
    os.system("pip3 install PyQt6")
    os.system("pip install PyQt6")
    os.system("python3 -m pip install PyQt6-sip")
    os.system("python3.11 -m pip install PyQt6-sip")
    os.system("pip3 install PyQt6-sip")
    os.system("pip install PyQt6-sip")
    os.system("pip3 install netaddr")
    os.system("pip install netaddr")
    os.system("python3 -m pip install netaddr")
    os.system("python3.11 -m pip install netaddr")
    os.system("pip3 install netifaces")
    os.system("pip install netifaces")
    os.system("python3 -m pip install netifaces")
    os.system("python3.11 -m pip install netifaces")
    os.system("pip3 install netifaces")
    os.system("pip install socket")
    os.system("python3 -m pip install socket")
    os.system("python3.11 -m pip install socket")
    os.system("pip3 install socket")


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QMainWindow, QGridLayout, QLabel, QLineEdit, QComboBox
import socket
import setuptools
import psutil



if choix != "1":
    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("La toolbox vivante")
            self.resize(300, 100)
            self.setup_ui()
            self.client_socket = socket.socket()
            self.client_socket.connect(('127.0.0.1', 10000))
            print("Connexion établie...")
            self.message = "rien"

        def setup_ui(self):


            # self.label = QLabel("Message : ")
            self.line_edit = QLineEdit("")
            self.button = QPushButton("Envoyer")
            self.button.clicked.connect(self.valider)
            # modifier la couleur de la zone de texte
            self.line_edit.setStyleSheet("background-color: white; color: black")
            self.text = QLabel("\n")
            self.text.setStyleSheet("padding: 5px 5px; background-color: white; color: black")
            
            self.quit = QPushButton("Quitter")
            self.quit.clicked.connect(self.__actionQuitter)
            self.button2 = QPushButton("Aide")
            self.button3 = QPushButton("CPU")
            self.button4 = QPushButton("RAM")
            self.button5 = QPushButton("OS")
            # self.button6 = QPushButton("Processus")
            self.button7 = QPushButton("Disk")
            self.button8 = QPushButton("IP")
            self.button9 = QPushButton("Port utilisé")
            self.button10 = QPushButton("Nom")
            self.line_edit2 = QLineEdit("")
            # self.button11 = QPushButton("Fermer")
            

            # une fenêtre apparaît quand on clique sur le bouton aide
            self.button2.clicked.connect(self.aide)
            self.button3.clicked.connect(self.cpu)
            self.button4.clicked.connect(self.ram)
            self.button5.clicked.connect(self.os)
            # self.button6.clicked.connect(self.processus)
            self.button7.clicked.connect(self.disk)
            self.button8.clicked.connect(self.ip)
            self.button9.clicked.connect(self.port)
            self.button10.clicked.connect(self.nom)
            # self.button11.clicked.connect(self.fermer)
            
            layout = QGridLayout()
            # layout.addWidget(self.label, 0, 0)
            layout.addWidget(self.line_edit, 0, 0)
            layout.addWidget(self.line_edit, 0, 0, 1, 0)
            layout.addWidget(self.button, 0, 1, 1, 1)
            layout.addWidget(self.text, 2, 0, 1, 2)
            layout.addWidget(self.quit, 13, 0, 1, 2)
            layout.addWidget(self.button2, 4, 0, 1, 1)
            layout.addWidget(self.button3, 5, 0, 1, 1)
            layout.addWidget(self.button4, 5, 1, 1, 1)
            layout.addWidget(self.button5, 7, 0, 1, 1)
            # layout.addWidget(self.button6, 8, 0, 1, 2)
            layout.addWidget(self.button7, 7, 1, 1, 1)
            layout.addWidget(self.button8, 11, 0, 1, 1)
            layout.addWidget(self.button9, 11, 1, 1, 1)
            layout.addWidget(self.button10, 4, 1, 1, 1)
            # layout.addWidget(self.button11, 13, 0, 1, 2)
            # layout.addWidget(self.line_edit2, 14, 0)
            # layout.addWidget(self.button12, 14, 1)
            # layout.addWidget(self.text2, 15, 0, 1, 2)
            self.setLayout(layout)

    

        def valider(self):
            self.message = self.line_edit.text()
            saisie = self.line_edit.text()
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText(f"Vous> {saisie}\nServeur> {data}")

        def aide(self):
            QMessageBox.information(self, "Aide", "Voici la liste des commandes que vous pouvez envoyez :\n- ping {adresse}\n- ls")

        def cpu(self):
            self.message = "cpu"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> CPU\nServeur> " + data + "% utilisés")

        def ram(self):
            self.message = "ram"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> RAM\nServeur> " + data + "% utilisés")

        def os(self):
            self.message = "os"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> OS\nServeur> " + data)

        def disk(self):
            self.message = "disk"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> DISK\nServeur> " + data)

        def ip(self):
            self.message = "ip"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> IP\nServeur> " + data)

        def port(self):
            self.message = "port"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> PORT\nServeur> " + data)

        def nom(self):
            self.message = "nom"
            self.client_socket.send(self.message.encode())
            print("Message envoyé... en attente d'une réponse")
            data = self.client_socket.recv(1024).decode()
            print(f"serveur : {data}")
            self.text.setText("Vous> NOM\nServeur> " + data)

        def closeEvent(self, event):
            self.client_socket.close()
            print("Connexion fermée")
            event.accept()

        def __actionQuitter(self):
            self.close()


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        app.exec()
