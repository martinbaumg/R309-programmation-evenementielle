import socket
import setuptools
import threading
import os
import platform
import psutil
import netaddr
import netifaces




message = "rien"

server_socket = socket.socket()
print("Socket crée, en attente du client...")
server_socket.bind(('127.0.0.1', 10000))
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















# import socket
# import threading
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost', 10008))
# server.listen(2)    

# def wait_for_client(server):
#     global clientconnected
#     global client
#     global address
#     print("Server is listening...")
#     print ("Waiting for client...")
#     while clientconnected == False:
#         client, address = server.accept()
#         print("Client connected: ", address)
#         clientconnected = True
#         client.send ("Hello Client".encode())

# def check_os(client):
#     global os
#     os = client.recv(1024).decode()
#     if os == "Linux":
#         print("This client is a Linux machine")
#     elif os == "Windows":
#         print("This client is a Windows machine")
#     elif os == "Darwin":
#         print("This client is a Mac machine")


# def receive_data(clientconnected, client, address):
#     while clientconnected == True:
#         data = client.recv(1024).decode()
#         print(f"client {address} send: {data}")
#         if data == "exit": # Close the connection when client send "exit" message
#             server.close()
#             print (f"Server closed by {address}")
#             break
#         elif data == "close":  # Close the client connection but not the server if client send "close"
#             print("Client disconnected")
#             client.close()
#             clientconnected = False 
#             print ("Waiting for client...")
#             while clientconnected == False: # Wait for a new client to connect
#                 client, address = server.accept()
#                 print("Client connected: ", address)
#                 clientconnected = True
#                 client.send ("Hello Client".encode())

# def send_data(clientconnected, client, address):
#     while clientconnected == True:
#         data = input("Enter message to send to client: ")
#         client.send(data.encode())
#         if data == "exit": # Close the connection when client send "exit" message
#             server.close()
#             print (f"Server closed by {address}")
#             break
#         elif data == "close":  # Close the client connection but not the server if client send "close"
#             print("Client disconnected")
#             client.close()
#             clientconnected = False 
#             print ("Waiting for client...")
#             while clientconnected == False: # Wait for a new client to connect
#                 client, address = server.accept()
#                 print("Client connected: ", address)
#                 clientconnected = True
#                 client.send ("Hello Client".encode())

# def main():
#     global clientconnected
#     global client
#     clientconnected = False
#     t1 = threading.Thread(target=wait_for_client, args=[server])
#     t1.start()
#     t1.join()   

#     os_thread = threading.Thread(target=check_os, args=[client])
#     os_thread.start()
#     os_thread.join()

#     t2 = threading.Thread(target=receive_data, args=[clientconnected, client, address])
#     t2.start()

#     t3 = threading.Thread(target=send_data, args=[clientconnected, client, address])
#     t3.start()

    

# if __name__ == '__main__':
#     main()




