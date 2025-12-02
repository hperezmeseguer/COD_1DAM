class Tablero:
    def __init__(self, tamano):
        if isinstance(tamano, int):
            self.dimensiones = (tamano, tamano)
        else:
            self.dimensiones = tamano