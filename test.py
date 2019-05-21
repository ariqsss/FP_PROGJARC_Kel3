"""
array=['']

tes = 'ses'
array.append(tes)

def client(IP):
    if IP not in array:
        array.append(IP)
        IPclient = "Client" + str((len(array) - 1 - array[::-1].index(IP)))
        return IPclient
    elif IP in array:
        IPclient = "Client" + str(array.index(IP))
        return IPclient

lol = client('boi')
print (array)

print (list(range(0,7)))
board = [None] + list(range(1, 10))

print(board[7], board[8], board[9])
print(board[4], board[5], board[6])
print(board[1], board[2], board[3])
print()
"""

b=int(input())
if b > 9:
    print("tada")