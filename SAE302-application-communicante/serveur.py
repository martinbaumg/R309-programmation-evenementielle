import socket
import setuptools
import threading
import os
import platform
import psutil
import netaddr
import netifaces

message = "rien"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("Entrer l'adresse IP du serveur : (appuyez sur ENTER pour avoir les valeurs par défaut) ")
if ip == "":
    ip = "127.0.0.1"
    port = 10000
else:
    port = int(input("Entrer le port du serveur : "))
server_socket.bind((ip, port))
print("Socket crée, en attente du client...")

server_socket.listen(1)


conn, address = server_socket.accept()
print("Connexion établie...")
while message != "q":
    message = conn.recv(1024).decode()
    print("Message reçu: ", message)

    if message == "cpu":
        cpu = psutil.cpu_percent()
        conn.send(str(cpu).encode())

    elif message == "ram":
        ram = psutil.virtual_memory().percent
        conn.send(str(ram).encode())

    elif message == "disk":
        disk = psutil.disk_usage('/').percent
        conn.send(str(disk).encode())

    elif message == "port":
        port = conn.getsockname()[1]
        conn.send(str(port).encode())

    elif message == "os":
        os = platform.system()
        conn.send(str(os).encode())

    elif message == "ip":
        netifaces.interfaces()
        adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr']
        netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
        conn.send(str(netaddr_adresse_ip).encode())

    elif message == "nom":
        nom = platform.node()
        conn.send(str(nom).encode())

    elif message == "salut":
        conn.send("salut ça va ?".encode())

    elif message.startswith("ls"):
        message = message.split(" ")
        if len(message) == 1:
            files = os.listdir()
            conn.send(str(files).encode())
        elif len(message) == 2:
            files = os.listdir(message[1])
            conn.send(str(files).encode())

    elif message.startswith("ping"):
        ip = message.split()[1]
        result = os.system("ping -c 2 " + ip)
        if result == 0:
            conn.send("ping vers {} réussi".format(ip).encode())
        else:
            conn.send("pas de réponse".encode())

    else:
        conn.send("Commande inconnue".encode())
