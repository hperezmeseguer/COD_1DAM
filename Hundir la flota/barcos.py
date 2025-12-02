class Barcos:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        if self.golpes_recibidos < self.longitud:
            self.golpes_recibidos += 1

    def esta_hundido(self):
        return self.golpess_recibidos >= self.longitud