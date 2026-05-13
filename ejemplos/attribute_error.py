try:
    texto = "Hola"
    longitud = texto.size  # El método correcto sería len(texto) o texto.__len__()
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")