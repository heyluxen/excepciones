modo_original = sistema.obtener_modo()
try:
    sistema.cambiar_modo("mantenimiento")
    realizar_actualizacion()
except ActualizacionError:
    print("La actualización falló")
finally:
    sistema.cambiar_modo(modo_original)  # Restauramos el modo original