nombre = ""
while nombre != "ANA" and nombre != "PEDRO" and nombre != "LUISA":
    nombre = input("Escribe tu nombre: ").upper()
if nombre == "ANA":
    print("Bienvenida ANA")
elif nombre == "PEDRO":
    print("Bienvenido PEDRO")
elif nombre == "LUISA":
    print("Bienvenida LUISA")