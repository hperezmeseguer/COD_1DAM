class Tablero:
    def __init__(self, tamano):
        if isinstance(tamano, int):
            self.dimensiones = (tamano, tamano)
        else:
            self.dimensiones = tamano

        filas, columnas = self.dimensiones

        self.casillas = [[0 for _ in range(columnas)] for _ in range(filas)]
