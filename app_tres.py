class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, punto1, punto2):
        self.esquina_superior_izquierda = punto1
        self.esquina_inferior_derecha = punto2

    def calcular_perímetro(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base == altura

# Crear puntos
punto1 = Punto(1, 3)
punto2 = Punto(5, 1)

# Crear rectángulo
rectangulo = Rectángulo(punto1, punto2)

# Calcular y mostrar perímetro y área
print("Perímetro:", rectangulo.calcular_perímetro())
print("Área:", rectangulo.calcular_área())

# Verificar si es un cuadrado
if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
