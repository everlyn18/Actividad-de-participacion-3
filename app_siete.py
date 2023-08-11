class Carta:
    PINTAS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return f"{self.valor} de {self.pinta}"

# Crear objetos de la clase Carta
carta1 = Carta("As", Carta.PINTAS[0])
carta2 = Carta("5", Carta.PINTAS[1])
carta3 = Carta("Reina", Carta.PINTAS[2])
carta4 = Carta("7", Carta.PINTAS[3])

# Imprimir las cartas
print(carta1)
print(carta2)
print(carta3)
print(carta4)
