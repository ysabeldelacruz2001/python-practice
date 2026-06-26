usuario = int(input("Edad: "))
if usuario >= 18:
    print("Puedes entrar al cine")
elif usuario >= 13:
    print("Puedes entrar solo con un adulto")
else:
    print("No puedes entrar")
