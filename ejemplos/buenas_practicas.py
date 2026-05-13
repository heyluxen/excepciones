# Mal ejemplo: bloque try demasiado grande
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    numeros = [int(x) for x in contenido.split()]
    resultado = sum(numeros) / len(numeros)
    print(f"El promedio es:{resultado}")
    archivo.close()
except:
    print("Ocurrió un error")

# Buen ejemplo: bloques try específicos
try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    print("El archivo 'datos.txt' no existe")
else:
    try:
        contenido = archivo.read()
        numeros = [int(x) for x in contenido.split()]
    except ValueError:
        print("El archivo contiene datos que no son números")
    else:
        try:
            resultado = sum(numeros) / len(numeros)
            print(f"El promedio es:{resultado}")
        except ZeroDivisionError:
            print("El archivo está vacío, no se puede calcular el promedio")
    finally:
        archivo.close()