from testclass import Person
import pickle


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

print (list(range(0,7)))"""

print (b''.join([b'line 1\n', b'line 2\n']))

board = [None] + list(range(1, 10))

def array():
    print(board[7], board[8], board[9])
    print(board[4], board[5], board[6])
    print(board[1], board[2], board[3])
    print()

board2 = [None]
board2.extend([2, 3, 2, 5, 6, 3, 3, 5, 6])

board = board2

array()
print (board)
DUMP = pickle.dumps(board)
print (DUMP)
print ('='*50)
LOAD = pickle.loads(DUMP)
print (LOAD)

"""
b=int(input())
if b > 9:
    print("tada")

# Here, we're creating a variable 'x', in the __main__ scope.
x = 'None!'


def func_A():
  # The below declaration lets the function know that we
  #  mean the global 'x' when we refer to that variable, not
  #  any local one

  global x
  #x = 'A'
  return x

def func_B():
  # Here, we are somewhat mislead.  We're actually involving two different
  #  variables named 'x'.  One is local to func_B, the other is global.

  # By calling func_A(), we do two things: we're reassigning the value
  #  of the GLOBAL x as part of func_A, and then taking that same value
  #  since it's returned by func_A, and assigning it to a LOCAL variable
  #  named 'x'.
  x = func_A() # look at this as: x_local = func_A()

  # Here, we're assigning the value of 'B' to the LOCAL x.
  x = 'B' # look at this as: x_local = 'B'

  return x # look at this as: return x_local

x1 = func_B()
print (x, x1)

decision = str(input("Play the game?(Y/n)"))
if decision == "Y":
  print ("OK")"""


p1 = Person("John", 36)

p1.age = 40
p2 = p1.myfunc()
p2