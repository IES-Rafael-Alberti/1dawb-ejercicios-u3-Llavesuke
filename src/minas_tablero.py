import random

# Acciones del jugador
MARCAR = "M"
REVELAR = "R"

# Dimensiones del tablero
FILAS = 8
COLUMNAS = 8
NUMERO_MINAS = 10

# Representación del tablero
VACIO = " "
MINA = "*"
BANDERA = "F"
VALOR_CELDA_DEFECTO = "."


def generar_tablero() -> list:
    """
    Esta función genera un tablero de juego vacío y coloca las minas en el tablero. Luego, calcula el número de minas adyacentes a cada celda.
    :return: tablero de juego
    """
    tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    #TODO: colocar las minas en el tablero
    colocar_minas(tablero)
    return tablero


def colocar_minas(tablero):
    """
    Esta función coloca las minas en el tablero de juego. Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.
    """
    mina = 0
    while mina != NUMERO_MINAS:
            i = random.randint(0,FILAS-1)
            j = random.randint(0,COLUMNAS-1)
            while tablero[i][j] == MINA:
                 i = random.randint(0,FILAS-1)
                 j = random.randint(0,COLUMNAS-1)
                 
            tablero[i][j] = MINA
            mina += 1

if __name__ == "__main__":
     tablero = generar_tablero()
     print(tablero)