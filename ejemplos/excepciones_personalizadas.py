class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""

    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo
        mensaje = f"No hay suficiente saldo. Saldo:{saldo}, Cantidad solicitada:{cantidad}"
        super().__init__(mensaje)

def retirar(cuenta, cantidad):
    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)
    cuenta.saldo -= cantidad
    return cuenta.saldo