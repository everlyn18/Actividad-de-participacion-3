class Punto:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia =math.sqrt((self.x - otro_punto.x)**2+(self.y - otro_punto.y)**2)
        return distancia
