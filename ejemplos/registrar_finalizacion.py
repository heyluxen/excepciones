try:
    registrar_inicio("tarea_diaria")
    ejecutar_tarea_diaria()
except Exception as e:
    registrar_error("tarea_diaria", str(e))
finally:
    registrar_finalizacion("tarea_diaria")  # Siempre registramos que terminó