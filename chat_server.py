import socket
import select
import threading
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = '127.0.0.1'
Port = 8080
server.bind((IP_address, Port)) 
#bind server ke IP address dengan port tertentu
server.listen(100)

list_of_clients=[]

def clientthread(conn, addr):
    conn.send(bytes("Welcome to this chatroom!", 'utf-8'))
    #mengirim pesan ke conn
    while True:
            try:     
                message = conn.recv(2048)
                if message:
                    print ("<" + ' '.join(map(str, addr)) + "> " + str(message, 'utf-8'))
                    message_to_send = "<" + addr[0] + "> " + str(message, 'utf-8')
                    broadcast(message_to_send,conn)

                else:
                    remove(conn)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(bytes(message, 'utf-8'))
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)
    print (addr[0] + " connected")

    threading.Thread(target=clientthread,args=(conn,addr)).start()

conn.close()
server.close()