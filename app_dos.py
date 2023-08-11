import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

# Crear dos instancias de la clase Punto
punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

# Mostrar coordenadas de los puntos
punto1.mostrar()
punto2.mostrar()

# Mover el punto1 a nuevas coordenadas
punto1.mover(1, 2)
punto1.mostrar()

# Calcular distancia entre punto1 y punto2
distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")
