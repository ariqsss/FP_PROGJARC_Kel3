import socket
import select
import sys
import msvcrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
#    exit()
IP_address = '127.0.0.1'#str(sys.argv[1])
Port = 8080#int(sys.argv[2])
server.connect((IP_address, Port))

while True:
    sockets_list = [server]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [], 1)
    if msvcrt.kbhit:
        print "Enter message:"
        read_sockets.append(sys.stdin)
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()