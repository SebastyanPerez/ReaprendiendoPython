class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        self.saldo = self.saldo - monto


c1=Cuenta(100)
c2=c1

c1.retirar(30)
print(c1.saldo)