
Tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
turno = 1
win = False

def check():
    global Tablero

    if (" " not in Tablero[0][0:3]) and (" " not in Tablero[1][0:3]) and (" " not in Tablero[2][0:3]):
        print("Empate")
        Tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        return False
            

    if Tablero[0][0] == "X" and Tablero[1][1] == "X" and Tablero[2][2] == "X":
        print("Gana X")
        return True
    
    if Tablero[0][0] == "O" and Tablero[1][1] == "O" and Tablero[2][2] == "O":
        print("Gana O")
        return True

    ## Horizontal
    for f in range(0,3):
        if Tablero[f][0] == "X" and Tablero[f][1] == "X" and Tablero[f][2] == "X":
            print("Gana X")
            return True
        
        if Tablero[f][0] == "O" and Tablero[f][1] == "O" and Tablero[f][2] == "O":
            print("Gana O")
            return True

    ## Vertical
    for c in range(0,3):
        if Tablero[0][c] == "X" and Tablero[1][c] == "X" and Tablero[2][c] == "X":
            print("Gana X")
            return True

        if Tablero[0][c] == "O" and Tablero[1][c] == "O" and Tablero[2][c] == "O":
            print("Gana O")
            return True
    return False




while win == False:
    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columan: "))


    for filas in range(0,3):
        for columnas in range(0,3):
            if (fila == filas) and (columna == columnas):
                if (turno%2) == 1:
                    Tablero[filas][columnas] = "X"
                    
                else:
                    Tablero[filas][columnas] = "O"
 
                print(Tablero[filas][columnas], end="")
            else:
                print(Tablero[filas][columnas], end="")
            
            if columnas<=1:
                print("|", end="")   
        print(" ")
    turno = turno + 1

    win = check()
