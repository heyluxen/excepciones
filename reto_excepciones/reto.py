def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        num1 = input("Introduce el primer número: ")
        num2 = input("Introduce el segundo número: ")
        
        # Convertir las entradas a números enteros
        a = int(num1)
        b = int(num2)
        
        # Realizar la división del primer número entre el segundo
        resultado = a / b
        
        # Devolver el resultado de la división (opcional, se puede imprimir)
        print(f"El resultado es: {resultado}")
        return resultado
    
    except ValueError:
        print("Error: Debes introducir un número válido")
    
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    
    finally:
        print("Operación finalizada")

# Llamada a la función
dividir_numeros()