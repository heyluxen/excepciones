def obtener_edad():
    while True:
        try:
            entrada = input("Introduce tu edad: ")

            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")

            edad = int(entrada)

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            if edad > 120:
                raise ValueError("La edad parece demasiado alta")

            return edad

        except ValueError as e:
            if str(e).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")
            else:
                print(f"Error:{e}")

# Uso
try:
    edad_usuario = obtener_edad()
    print(f"Tu edad es:{edad_usuario}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")