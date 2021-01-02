from copy import deepcopy
def checkearPalabra(tablero, palabra, orientacion, i, j):
    largoP = len(palabra)
    bandera = True
    for k in range(largoP):
            if(tablero[i + k * orientacion[0]][j + k * orientacion[1]] != ' ' and tablero[i + k * orientacion[0]][j + k * orientacion[1]] != palabra[k]):
                bandera = False
                break
    return bandera
def ubicacionDisponible(tablero, palabra, orientacion, yaUsadas):
    dimension = len(tablero)
    largoP= len(palabra)
    I = -1
    J = -1
    if(largoP <= dimension):
        if(orientacion[0] == -1):
            inicioI = largoP - 1
            maxI = dimension
        else:
            inicioI = 0
            maxI = dimension - ((largoP - 1) * orientacion[0])
        maxJ = dimension - ((largoP - 1) * orientacion[1])
        for i in range(inicioI, maxI):
            for j in range(maxJ):
                if((tablero[i][j] == ' ' or tablero[i][j] == palabra[0]) and not (i,j) in yaUsadas):
                    if(checkearPalabra(tablero, palabra, orientacion,i, j)):
                        I = i
                        J = j
                        break
            if(I != -1):
                break
    return (I,J)

def insertarPalabra(tablero, palabra, orientacion, i, j):
    Tablero = deepcopy(tablero)
    largoP = len(palabra)
    for k in range(largoP):
        Tablero[i + (k * orientacion[0])][j + (k * orientacion[1])] = palabra[k]
    return Tablero

def generarTableroDePalabras(tablero, palabras):
    Tablero = deepcopy(tablero)
    print('------------------temp')
    imprimirTablero(tablero)
    if(palabras):
        yaUsadas = []
        posible = ubicacionDisponible(Tablero, palabras[0][0], palabras[0][1], yaUsadas)
        while(posible != (-1,-1)):
            tableroTemp = insertarPalabra(Tablero, palabras[0][0], palabras[0][1], posible[0], posible[1])
            tableroTemp2 = generarTableroDePalabras(tableroTemp, palabras[1:])
            #print('------------------temp')
            #imprimirTablero(tableroTemp)
            #print('------------------temp2')
            #imprimirTablero(tableroTemp2)
            if(tableroTemp2 == tableroTemp):
                yaUsadas += [posible]
                posible = ubicacionDisponible(tablero, palabras[0][0], palabras[0][1], yaUsadas)
            else:
                Tablero = deepcopy(tableroTemp2)
                posible = (-1,-1)
    #imprimirTablero(tablero)
    return Tablero

def imprimirTablero(tablero):
    print('\n'.join(map((lambda x: ''.join(x)), tablero)))


t = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
palabras = [('hola', (1,1)),('casa', (0,1)),('linda', (1,1)),('maxi', (-1,1)),('gato', (1,0))]
imprimirTablero(generarTableroDePalabras(deepcopy(t), palabras))