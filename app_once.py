class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron ${cantidad} en la cuenta. Nuevo balance: ${self.balance}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron ${cantidad} de la cuenta. Nuevo balance: ${self.balance}")
        else:
            print("Fondos insuficientes para realizar el retiro.")
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2% (${cuota}) a la cuenta. Nuevo balance: ${self.balance}")
    
    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: ${self.balance}")

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan Perez", "Maria Gomez"], 1000.0)
cuenta1.mostrar_detalles()
