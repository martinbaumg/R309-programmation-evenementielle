import socket
import setuptools
import threading
import os
import platform
import psutil
import netaddr
import netifaces
import shutil
import subprocess

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
while message != "":
    message = conn.recv(1024).decode()
    print("Message reçu: ", message)

    if message == "cpu":
        cpu = psutil.cpu_percent()
        conn.send(str(cpu).encode())

    elif message == "ram":
        ram = psutil.virtual_memory().percent
        conn.send(str(ram).encode())

    elif message == "stockage":
        disk = shutil.disk_usage("/")
        disk = disk.free / disk.total * 100
        # garder uniquement 2 chiffres après la virgule
        disk = round(disk, 2)
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

    elif message.startswith("python --v"):
        version = platform.python_version()
        conn.send(str(version).encode())

    elif message.startswith("dir"):
        if platform.system() == "Windows":
            os.system("dir")
            conn.send("Commande dir".encode())
        else:
            conn.send("Inompatable avec l'OS".encode())

    # elif message.startswith("ls") and platform.system() == "Darwin":
    #     message = message.split(" ")
    #     if len(message) == 1:
    #         files = os.listdir()
    #         conn.send(str(files).encode())
    #     elif len(message) == 2:
    #         files = os.listdir(message[1])
    #         conn.send(str(files).encode())

    elif message.startswith("ping"):
        ip = message.split()[1]
        result = os.system("ping -c 1 " + ip)
        if result == 0:
            conn.send("ping vers {} réussi".format(ip).encode())
        else:
            conn.send("pas de réponse".encode())


    # else:
    #     try:
    #         command = message
    #         output = subprocess.check_output(command, shell=True)
    #         if output != 0:
    #             output = "Commande exécutée"
    #         else:
    #             conn.send(output)
    #     except Exception as e:
    #         conn.send(f"Error returned by server: {e}".encode('utf-8'))


    # else:
    #     os.system(message)
    #     result = int(subprocess.getoutput(os.system(message)).listen("True"))
    #     if result != 0:
    #         conn.send("Commande exécutée".encode())
    #     else :
    #         conn.send("Commande inconnue ou incompatible avec l'OS".encode())


    # else:
    #     os.system(message)
    #     result = os.popen(message).read()
    #     if result != 0:
    #         conn.send("Commande exécutée".encode())
    #     else :
    #         conn.send("Commande inconnue ou incompatible avec l'OS".encode())

    # else:
    #     cmd = os.popen(message).read()
    #     var = os.system(message)
    #     if var != 0:
    #         conn.send("Commande inconnue".encode())
    #     else:
    #         conn.send(cmd.encode())
    # print("Message envoyé: ", message)

    else:
        cmd = message
        verif = os.system(cmd)
        print(verif)
        msg = os.popen(cmd).read()
        print(f'----------- {msg}')
        if verif == 0:
            if msg != "":
                conn.send(msg.encode())
            else:
                conn.send(f"{cmd} éxecuté avec succès".encode())
        else:
            msg=str(f'{cmd} commande impossible')
            conn.send(msg.encode())
