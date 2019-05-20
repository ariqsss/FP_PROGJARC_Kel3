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