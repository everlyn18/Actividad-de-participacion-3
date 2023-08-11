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

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan Perez", "Maria Gomez"], 1000.0)
cuenta1.depositar(500)   # Output: Se depositaron $500 en la cuenta. Nuevo balance: $1500.0
cuenta1.depositar(-200)  # Output: La cantidad a depositar debe ser mayor que cero.
