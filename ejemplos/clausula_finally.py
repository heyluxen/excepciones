try:
    archivo = open("registro.txt", "w")
    archivo.write("Operación iniciada\n")
    # Código que podría generar una excepción
    resultado = 10 / int(input("Introduce un número: "))
    archivo.write(f"Resultado:{resultado}\n")
except ZeroDivisionError:
    archivo.write("Error: División por cero\n")
except ValueError:
    archivo.write("Error: Valor no válido\n")
finally:
    archivo.write("Operación finalizada\n")
    archivo.close()  # El archivo se cierra siempre
    print("Proceso completado")