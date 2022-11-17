import socket

message = "rien"


client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 10000))
print("Connexion établie...")

menu = input("Menu général, que voulez-vous faire ?\n1. Envoyer un message\n2. Quitter\n")

if menu == "1" :
    while message != "quit":
        message = input("que voulez-vous envoyer : ")
        print("Message envoyé... en attente d'une réponse")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Message reçu : {data}")

code = input("voulez vous quitter ? (y/n) : ")

if code == "y" or menu =="2" or message == "quit":
    client_socket.close()

# else :
#     message = input("que voulez-vous envoyer : ")
#     client_socket.send(message.encode())
#     data = client_socket.recv(1024).decode()
#     print(f"Message reçu : {data}")


