import socket

message = "rien"


client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 10000))
print("Connexion établie...")


while message != "q":
    message = input("vous (q pour quitter) : ")
    client_socket.send(message.encode())
    print("Message envoyé... en attente d'une réponse")
    data = client_socket.recv(1024).decode()
    print(f"serveur : {data}")


if message == "q":
    client_socket.close()

