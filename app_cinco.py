import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_al_centro <= self.radio

# Crear un objeto de la clase Circulo
centro = (0, 0)
radio = 5
mi_circulo = Circulo(centro, radio)

# Calcular y mostrar el área y el perímetro
area = mi_circulo.calcular_area()
perimetro = mi_circulo.calcular_perimetro()
print("Área:", area)
print("Perímetro:", perimetro)

# Verificar si un punto pertenece al círculo
punto1 = (2, 2)
punto2 = (6, 6)
print("El punto", punto1, "pertenece al círculo:", mi_circulo.punto_pertenece(punto1))
print("El punto", punto2, "pertenece al círculo:", mi_circulo.punto_pertenece(punto2))  