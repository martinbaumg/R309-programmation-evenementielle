import socket


message = "rien"

server_socket = socket.socket()
print("Socket crée, en attente du client...")
server_socket.bind(('127.0.0.1', 10000))
server_socket.listen(1)


conn, address = server_socket.accept()
print("Connexion établie...")
while message != "q":
    reply = input("vous (q pour quitter) : ")
    print("Message envoyé... en attente d'une réponse")
    data = conn.recv(1024).decode()
    conn.send(reply.encode())
    print(f"de {address} : {data}")


if message == "q":
    conn.close()
    server_socket.close()
