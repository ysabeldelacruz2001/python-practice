edad = int(input("Edad: "))
entrada = input("Tipo de entrada (VIP / NORMAL / NINGUNA): ").upper()
if edad >= 18:
    if entrada == "VIP":
        print("Entrada VIP, disfruta del concierto")
    elif entrada == "NORMAL":
        print("Entrada general, disfruta del concierto")
    else:
        print("No puedes ingresar sin entradas")
else:
    print("No puedes ingresar al concierto")