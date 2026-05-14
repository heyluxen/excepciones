def retirar_dinero(cuenta, cantidad):
    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    if cantidad > cuenta.saldo:
        raise ValueError("Saldo insuficiente")

    cuenta.saldo -= cantidad
    return cuenta.saldo