edad = int(input("Edad: "))
ingreso_mensual = int(input("Ingreso mensual: "))

if edad >= 18:
    if ingreso_mensual >= 1500:
        print("Solicitud aprobada")
    else:
        print("Solicitud rechazada por fondos insuficientes")
else:
    print("No puedes solicitar la tarjeta")
