try:
    # Código que podría fallar
    resultado = eval(input("Introduce una expresión: "))
except Exception as e:
    print(f"Error de tipo:{type(e).__name__}")
    print(f"Descripción:{e}")