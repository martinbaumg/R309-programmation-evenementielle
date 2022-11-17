import socket


message = "rien"

server_socket = socket.socket()
print("Socket crée, connexion en cours...")
server_socket.bind(('127.0.0.1', 10000))
server_socket.listen(1)

print("Connexion établie...")

menu = input("Menu général, que voulez-vous faire ?\n1. Envoyer un message\n2. Quitter\n")

if menu == "1":
     conn, address = server_socket.accept()
     while message != "quit":
        reply = input("que voulez-vous envoyer : ")
        print("Message envoyé... en attente d'une réponse")
       
        data = conn.recv(1024).decode()
        conn.send(reply.encode())
        print(f"Message reçu : {data}")

code = input("voulez vous quitter ? (y/n) : ")

if code == "y" or menu =="2" or message == "quit":
    conn.close()
    server_socket.close()

# else : 
#     reply = input("que voulez-vous envoyer : ")
#     conn.send(reply.encode())
#     data = conn.recv(1024).decode()
#     print(f"Message reçu : {data}")
