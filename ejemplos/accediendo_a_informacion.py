try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    print(f"Error:{error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")