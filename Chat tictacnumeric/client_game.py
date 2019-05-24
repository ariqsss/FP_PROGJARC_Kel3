import socket
import select
import sys
import msvcrt
import pickle

flag = 1

finish = 0
board = [None] + list(range(1, 10))
number = []
sets = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
]

def draw():
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print()

def check_number(b, flag):
    if b > 0 and b < 10:
        if b not in number:
            if flag == 0 and (b % 2) == 0:
                number.append(b)
                return True
            elif flag == 1 and (b % 2) == 1:
                number.append(b)
                return True
            elif flag == 0 and (b % 2) == 1:
                return ("\nYou must insert the opposite (Even) number. Try again")
            elif flag == 1 and (b % 2) == 0:
                return ("\nYou must insert the opposite (Odd) number. Try again")
        elif b in number:
            return ("\nNumber already exist. Try again")
    else:
        return ("\nIncorrect number. Try again")

def choose_number():

    def change_flag(flag):
        if (flag == 0):
            flag = 1
        elif (flag == 1):
            flag = 0
        return flag

    draw()
    while True:
        try:

            global flag
            a = int(input())
            if a > 0 and a < 10:
                if a in board:
                    b = int(input("Pick your number:"))
                    number_validation = check_number(b, flag)
                    if (number_validation == True):
                        flag = change_flag(flag)
                        return a, b
                    else:
                        print(number_validation)
                else:
                    print("\nField already taken. Try again")
            else:
                print("\nField not exist. Try again")

        except ValueError:
            print("\nThat's not a number. Try again")

def is_game_over():

    if finish == 9:
        print("game over\n")
        return True

def calculate():
    maxx = 0
    maxo = 0

    for a, b, c in sets:
        scorex = 0
        scoreo = 0
        if 'X' in board[a]:
            scorex += int(board[a][1])
        if 'X' in board[b]:
            scorex += int(board[b][1])
        if 'X' in board[c]:
            scorex += int(board[c][1])
        if 'O' in board[a]:
            scoreo += int(board[a][1])
        if 'O' in board[b]:
            scoreo += int(board[b][1])
        if 'O' in board[c]:
            scoreo += int(board[c][1])
        if scorex > maxx:
            maxx = scorex
        if scoreo > maxo:
            maxo = scoreo
        print("%d %d %d : X= %d O= %d" % (a, b, c, scorex, scoreo))
    print("Player X highest score:%d\nPlayer O highest score:%d" % (maxx, maxo))
    if (maxx > maxo):
        print("X wins the game")
    if (maxo > maxx):
        print("O wins the game")
    if (maxx == maxo):
        print("The game draw")

"""
    for player in 'XO' * 9:
        draw()
        if is_game_over():
            calculate()
            break
        print("Player {0} pick your move".format(player))
        a, b = choose_number()
        c = str(b)
        board[a] = player + c
        finish += 1
        print()
"""


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = '10.151.254.200'
Port = 3333
server.connect((IP_address, Port))

#decision = input("Play the game?(Y/n)")
#if decision == "Y":
while True:
    sockets_list = [server]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [], 1)
    if msvcrt.kbhit:
#       print ("Enter message:")
        read_sockets.append(sys.stdin)
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            message, load_field = [int(i) for i in socks.recv(2048).decode('utf-8').split('\n')]
            load_message = pickle.loads(load_field)
            print (str(message, 'utf-8'))
        else:
            #while True
            #for player in 'XO' * 9:
            draw()
            if is_game_over():
                calculate()
                sys.exit()
            print("Player X pick your move")
            # field = int(input())
            # value = int(input("Pick your number:"))
            a, b = choose_number()
            c = str(b)
            board[a] = "X" + c
            finish += 1
            print()

            message = pickle.dumps(board)
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(str(message))
            sys.stdout.write("\n")
            sys.stdout.flush()

server.close()

#elif decision == "n":
#    sys.exit()