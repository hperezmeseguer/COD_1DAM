class Tablero:
    def __init__(self, tamano):
        if isinstance(tamano, int):
            self.dimensiones = (tamano, tamano)
        else:
            self.dimensiones = tamano

        filas, columnas = self.dimensiones

        self.casillas = [[0 for _ in range(columnas)] for _ in range(filas)]

    def mostrar_tablero(self):
        print("TABLERO")
        for fila in self.casillas:
            print(" ".join(str(casilla) for casilla in fila))
        print("-" * 20)

# PRUEBA
if __name__ == "__main__":
    tablero = Tablero(6)
    tablero.mostrar_tablero()