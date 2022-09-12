class Usuario:
    def __init__(self,nombre,email,saldo) -> None:
        self.nombre=nombre
        self.email=email
        self.saldo=saldo

    def hacer_deposito(self,monto):
        self.saldo=self.saldo+monto
        return self
        

    def hacer_retiro(self, monto):
        self.saldo=self.saldo-monto
        return self

    def mostrar_balance_usuario(self): 
        print(self.saldo)
        return self

    def  transfer_dinero(self, other_user, monto): 
        self.hacer_retiro(monto)
        other_user.hacer_deposito(monto)
        return self