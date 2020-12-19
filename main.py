def checkearPalabra(tablero, palabra, orientacion, i, j):
    largoP = len(palabra)
    bandera = True
    for k in range(largoP):
            if(tablero[i + k * orientacion[0]][j + k * orientacion[1]] != ' ' and tablero[i + k * orientacion[0]][j + k * orientacion[1]] != palabra[k]):
                bandera = False
                break
    return bandera

def ubicacionDisponible(tablero, palabra, orientacion):
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
                if(tablero[i][j] == ' ' or tablero[i][j] == palabra[0]):
                    print(checkearPalabra(tablero, palabra, orientacion,i, j))
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
        tablero[i + k * orientacion[0]][j + k * orientacion[1]] = palabra[k]
    return tablero

tablero = [['a','h','h','t','r','a',],['r','h',' ','b',' ',' ',],[' ',' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',' ',]]
p = ubicacionDisponible(tablero, "hola", (-1,1))
print(insertarPalabra(tablero, "hola", (-1,1), p[0], p[1]))