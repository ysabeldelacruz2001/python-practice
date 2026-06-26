usuario = int(input("Ingresa tu nota (1 al 20): "))
if usuario < 1 or usuario > 20:
    print("La nota debe estar entre 1 y 20")
elif usuario >= 18:
    print("Excelente alumno, ¡Aprobaste con honores!")
elif usuario >= 14:
    print("Aprobado")
else:
    print("Desaprobado")
