def updateList(lista):
    del lista[:1]
    print(lista)

def receiveList(lista):
    updateList(lista)
    print (lista)

receiveList([0,1,2,3,4,5])