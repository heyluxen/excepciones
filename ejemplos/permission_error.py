try:
    with open("/etc/passwd", "w") as archivo:  # Intentar escribir en un archivo protegido
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")