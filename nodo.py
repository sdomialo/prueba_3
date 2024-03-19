class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def obtener_valor(self):
        return self.valor

    def obtener_siguiente(self):
        return self.siguiente

    def establecer_siguiente(self, siguiente):
        self.siguiente = siguiente