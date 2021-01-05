import random

def generarTableroVacio(dimension):
    return [[' ' for _ in range(dimension)] for _ in range(dimension)]

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
    largoP = len(palabra)
    for k in range(largoP):
        tablero[i + (k * orientacion[0])][j + (k * orientacion[1])] = palabra[k]
    return tablero

def eliminarPalabra(tablero, palabra, orientacion, posicion):
    largoP = len(palabra)
    i = posicion[0]
    j = posicion[1]
    for k in range(largoP):
        if(tablero[i + (k * orientacion[0])][j + (k * orientacion[1])] == palabra[k]):
            tablero[i + (k * orientacion[0])][j + (k * orientacion[1])] = ' '
    return tablero

def letraValida(tablero, palabras, i, j):
    dimension = len(tablero)
    retorno = False
    substring = tablero[i][j]
    for palabra in palabras:
        if(not substring in palabra[0]):
            palabras.remove(palabra)
    for palabra in palabras:
        substring = tablero[i][j]
        extremos = [(i,j),(i,j)]
        bandera = True
        bDer = True
        bIzq = True
        while(substring in palabra[0] and bandera):
            if(bDer):
                movIDer = extremos[1][0] + palabra[1][0]
                movJDer = extremos[1][1] + palabra[1][1]
                if(movIDer >= 0 and movIDer < dimension and movJDer >= 0 and movJDer < dimension):
                    if((substring + tablero[movIDer][movJDer]) in palabra[0]):
                        substring += tablero[movIDer][movJDer]
                        extremos[1] = (movIDer,movJDer)
                    else:
                        bDer = False
                else:
                    bDer = False
            if(bIzq):
                movIIzq = extremos[0][0] - palabra[1][0]
                movJIzq = extremos[0][1] - palabra[1][1]
                if(movIIzq >= 0 and movIIzq < dimension and movJIzq >= 0 and movJIzq < dimension):
                    if((substring + tablero[movIIzq][movJIzq]) in palabra[0]):
                        tablero[movIIzq][movJIzq] += substring
                        extremos[0] = (movIIzq,movJIzq)
                    else:
                        bIzq = False
                else:
                    bIzq = False
            bandera = bDer or bIzq
        if(substring == palabra[0]):
            retorno = True
            break
    return retorno
        
def rellenarVacios(tablero, palabras):
    alfabeto = ["a","b","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    dimension = len(tablero)
    insertarLetra = False
    for i in range(dimension):
        for j in range(dimension):
            if(tablero[i][j] == ' '):
                random.shuffle(alfabeto)
                k = 0
            while(tablero[i][j] == ' ' and  k < 25):    
                tablero[i][j] = alfabeto[k]
                if(letraValida(tablero, palabras, i, j)):
                    k += 1
                    tablero[i][j] = ' '
    return tablero

def generarTableroDePalabras(dimension, palabras):
    tablero = generarTableroVacio(dimension)
    yaUsadas = {}
    for palabra in palabras:
        yaUsadas[palabra[0]] = []
    i = 0
    while( i < len(palabras)):
        posible = ubicacionDisponible(tablero, palabras[i][0], palabras[i][1], yaUsadas[palabras[i][0]])
        if(posible == (-1,-1)):
            i -= 1
            if(i == -1):
                break
            else:
                tablero = eliminarPalabra(tablero, palabras[i][0], palabras[i][1],yaUsadas[palabras[i][0]][-1])
                i -= 1
        else:
            tablero = insertarPalabra(tablero,palabras[i][0], palabras[i][1], posible[0],posible[1])
            yaUsadas[palabras[i][0]] += [posible]
        i += 1
    return tablero

def imprimirTablero(tablero):
    print('\n'.join(map((lambda x: ''.join(x)), tablero)))

def generarTablero(dimension, palabras):
    noSePudoRellenar = False
    tablero = generarTableroDePalabras(dimension, palabras)
    if(tablero != generarTableroVacio(dimension)):
        tablero = rellenarVacios(tablero, palabras)
    for fila in tablero:
        for caracter in fila:
            if(caracter == ' '):
                noSePudoRellenar = True
                break
        if(noSePudoRellenar):
            tablero = generarTableroVacio(dimension)
            break
    return tablero

def procesarLinea(linea):
    orientacion = int(linea[-1])
    palabra = linea[:-2]
    if(orientacion == 1 or orientacion == 3):
        palabra = palabra[::-1]
    if(orientacion < 2):
        orientacion = (0,1)
    elif(orientacion < 4):
        orientacion = (1,0)
    elif(orientacion == 4):
        orientacion = (1,1)
    elif(orientacion == 5):
        orientacion = (-1,1)
    return (palabra, orientacion)
    

def procesarEntrada(lineas):
    lineas = list(map((lambda x: x[:-1]), lineas))
    dimension = lineas[1]
    lineas = lineas[3:]
    palabras = list(map(procesarLinea, lineas))
    return (dimension, palabras)
        

def leerEntrada(archivo):
    f = open(archivo, 'r')
    lineas = f.readlines()
    f.close()
    return  procesarEntrada(lineas)

def procesarLemario(lineas):
    lineas = map((lambda x: x[:-1]),lineas)
    lineas = list(filter((lambda x: len(x) > 1), lineas))
    return lineas

def leerLemario(archivo):
    f = open(archivo, 'r')
    lineas = f.readlines()
    f.close()
    return procesarLemario(lineas)

def validarPalabras(lemario, palabras):
    for i in range(len(palabras)):
        if(not palabras[i][0] in lemario):
            soloPalabras = set(map((lambda x: x[0]), palabras))
            noRepetidas = set(lemario) - soloPalabras
            if(noRepetidas):
                palabras[i]= (random.sample(noRepetidas,1)[0], palabras[i][1])
            else:
                palabras.remove(palabras[i])
    return palabras

#t = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
palabras = [('hola', (1,1)),('casa', (0,1)),('linda', (1,1)),('maxi', (-1,1)),('gato', (1,0)),('nico',(0,1))]
palabras.sort(reverse=True,key=(lambda x: len(x[0])))
print(palabras)
t = generarTablero(6, palabras)
imprimirTablero(t)
#mprimirTablero(rellenarVacios(t, palabras))


