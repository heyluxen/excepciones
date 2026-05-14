def dividir(a, b):
    try:
        resultado = a / b
        return resultado  # Este return no se ejecuta inmediatamente
    except ZeroDivisionError:
        print("Error: División por cero")
        return None  # Este return tampoco se ejecuta inmediatamente
    finally:
        print("División finalizada")  # Esto se ejecuta antes de cualquier return
        # Ahora sí se devuelve el valor correspondiente

print(dividir(10, 2))  # Imprime "División finalizada" y luego 5.0
print(dividir(10, 0))  # Imprime "Error: División por cero", "División finalizada" y luego None