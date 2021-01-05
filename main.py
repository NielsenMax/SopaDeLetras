import random

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

def generarTableroDePalabras(tablero, palabras):
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

#TODO usar posicionesLetras para ver si anda
def letraExtremo(letras, orientacion, sentido):
    extremo = letras[0]
    for v in letras[1:]:
        

def formaPalabra(tablero, palabra, orientacion, substring, posicionesLetras):
    print(substring)
    dimension = len(tablero)
    retorno = False
    if(substring == palabra):
        retorno = True
    elif(substring in palabra):
        letraMaxDerecha = letraExtremo(posicionesLetras, orientacion, 1)
        movIDer = letraMaxDerecha[0} + orientacion[0]
        movJDer = letraMaxDerecha[1] + orientacion[1] 
        if(movIDer > 0 and movIDer < dimension and movJDer > 0 and movJDer < dimension):
            retornoDer = formaPalabra(tablero, palabra, orientacion, substring + tablero[movIDer][movJDer], posicionesLetras += [(movIDer,movJDer)])
        else:
            retornoDer = False
        letraMaxIzquierda = letraExtremo(posicionesLetras, orientacion, -1)
        movIIzq = letraMaxIzquierda[0] - orientacion[0]
        movJIzq = letraMaxIzquierda[1] - orientacion[1] 
        if(movIIzq > 0 and movIIzq < dimension and movJIzq > 0 and movJIzq < dimension):
            retornoIzq = formaPalabra(tablero, palabra, orientacion, substring + tablero[movIIzq][movJIzq], posicionesLetras += [(movIIzq,movJIzq)])
        else:
            retornoIzq = False
        retorno = retorno or retornoDer or retornoIzq
    return retorno
#TODO que anda la funcion anterior

def letraValida(tablero, palabras, i, j):
    palabrasPropias = []
    dimension = len(tablero)
    retorno = False 
    for palabra in palabras:
        if(tablero[i][j] in palabra[0]):
            palabrasPropias += [palabra]
    for palabra in palabrasPropias:
        if(retorno):
            break
        movIDer = i + palabra[1][0]
        movJDer = j + palabra[1][1]
        if(movIDer >= 0 and movIDer < dimension and movJDer >= 0 and movJDer < dimension):
            retornoDer = formaPalabra(tablero, palabra[0], palabra[1], tablero[i][j] + tablero[movIDer][movJDer])
        else:
            retornoDer = False
        movIIzq = i - palabra[1][0]
        movJIzq = j - palabra[1][1] 
        if(movIIzq >= 0 and movIIzq < dimension and movJIzq >= 0 and movJIzq < dimension):
            retornoIzq = formaPalabra(tablero, palabra[0], palabra[1], tablero[i][j] + tablero[movIIzq][movJIzq])
        else:
            retornoIzq = False
        retorno = retornoDer or retornoIzq
    return retorno
        
def rellenarVacios(tablero, palabras):
    alfabeto = {"a","b","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    dimension = len(tablero)
    for i in range(dimension):
        for j in range(dimension):
            if(tablero[i][j] == ' '):
                insertarLetra = True
            while(insertarLetra):    
                tablero[i][j] = random.choice(tuple(alfabeto))
                insertarLetra = not letraValida(tablero, palabras, i, j)
    return tablero

def imprimirTablero(tablero):
    print('\n'.join(map((lambda x: ''.join(x)), tablero)))

t = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
palabras = [('hola', (1,1)),('casa', (0,1)),('linda', (1,1)),('maxi', (-1,1)),('gato', (1,0)),('nico',(0,1))]
imprimirTablero(generarTableroDePalabras(t, palabras))
t[1][2] = 'z'
print(letraValida(t, palabras, 0, 1))


