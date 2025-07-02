from collections import defaultdict

TIPOS_DULCES = ['A', 'B', 'C']

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dulces = defaultdict(int)
        self.chupetines = 0
        self.salvado = False

    def recibir_dulces(self):
        for _ in range(2):
            tipo = TIPOS_DULCES[ord(self.nombre[0]) % 3]  # Para hacerlo determinista
            self.dulces[tipo] += 1

    def canjear_dulces(self):
        if all(self.dulces[tipo] >= 1 for tipo in TIPOS_DULCES):
            for tipo in TIPOS_DULCES:
                self.dulces[tipo] -= 1
            self.chupetines += 1
            self.salvado = True
            return True
        else:
            return False

    def dar_dulce_extra(self, tipo):
        self.dulces[tipo] += 1

    def tiene_dulce(self, tipo):
        return self.dulces[tipo] > 0

    def quitar_dulce(self, tipo):
        if self.dulces[tipo] > 0:
            self.dulces[tipo] -= 1
            return True
        return False

    def dar_dulce(self, tipo):
        self.dulces[tipo] += 1

    def mostrar_inventario(self):
        return f"{self.nombre} | Dulces: {dict(self.dulces)}, Chupetines: {self.chupetines}, Salvado: {self.salvado}"
