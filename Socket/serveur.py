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
# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 10000))
# server.listen(5)
# print("Server is listening...")
# clientconnected = False
# print ("Waiting for client...")

# # Wait for a client to connect
# while clientconnected == False:
#     client, address = server.accept()
#     print("Client connected: ", address)
#     clientconnected = True
#     client.send ("Hello Client".encode())

# # Receive data from the client when client connected
# while clientconnected == True:
#     data = client.recv(1024).decode()
#     print(f"Client {address} send: {data}")
#     if data == "exit": # Close the connection when client send "exit" message
#         server.close()
#         print (f"Server closed by {address}")
#         break
#     elif data == "close":  # Close the client connection but not the server if client send "close"
#         print("Client disconnected")
#         client.close()
#         clientconnected = False 
#         print ("Waiting for client...")
#         while clientconnected == False: # Wait for a new client to connect
#             client, address = server.accept()
#             print("Client connected: ", address)
#             clientconnected = True
#             client.send ("Hello Client".encode())

# if __name__ == '__main__':
#     pass