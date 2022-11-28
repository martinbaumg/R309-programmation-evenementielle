import socket
import select
import errno
import time

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 10000

data = "rien"
my_username = input("Nom: ")

client_socket = socket.socket()
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


while True:
    message = input(f'{my_username} > ')
    # Pour avoir un lecteur de message mettre en commentaire la ligne du dessus et décommenter celle du dessous
    # message = ""


    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connexion fermée par le serveur')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Erreur: {}'.format(str(e)))
            sys.exit()
        continue
    except Exception as e:
        print('Erreur: '.format(str(e)))
        sys.exit()