try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    print("Archivo leído correctamente.")
    archivo.close()  # Solo cerramos si se abrió con éxito