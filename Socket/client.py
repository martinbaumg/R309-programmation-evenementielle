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

# import socket

# # Create one client socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 10000))
# print(f"Client connected to server")
# client.send("Hello Server".encode())
# data = client.recv(1024).decode()
# print(data)

# while True:
#     message = input("Enter your message: ") # Possible to send message to the server
#     client.send(message.encode())
#     if message == "exit": # Close the server when client send "exit" message
#         client.close()
#         break
#     elif message == "close": # Close the client connection but not down the server if client send "close"
#         print ("Client disconnected")
#         break

# if __name__ == '__main__':
#     pass