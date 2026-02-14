class CuentaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo  # Encapsulado: atributo privado
        self.limite = limite

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad inválida para depositar.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo and cantidad <= self.limite:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Retiro inválido. Verifica el saldo o el límite.")

    def consultar_saldo(self):
        return self.__saldo

# Ejemplo de uso
cuenta = CuentaBancaria("Sebas", 100, 50)
cuenta.depositar(30)
cuenta.retirar(20)
print("Saldo actual:", cuenta.consultar_saldo())
# cuenta.__saldo = 1000  # Esto no funciona, el saldo está encapsulado