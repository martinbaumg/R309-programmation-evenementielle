import socket

message = "rien"


client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 10000))
print("Connexion établie...")


while message != "bye":
    message = input("vous (bye pour quitter) : ")
    client_socket.send(message.encode())
    print("Message envoyé... en attente d'une réponse")
    data = client_socket.recv(1024).decode()
    print(f"serveur : {data}")


if message == "bye":
    conn.close()

if message == "reset":
    serveur_socket.close()


