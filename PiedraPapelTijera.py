import random

UserVidas = 3
PCVidas = 3
pc = random.randint(1, 3)

while UserVidas or PCVidas != 0:
    print("*" * 40)
    user = int(input("INGRESA UN NUMERO \n1 Piedra \n2 Papel \n3 Tijera \n"))
    # ELECCION DE NOMBRE
    Nombres = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera"
    }
    if user in Nombres:
        print(f"Haz elegido {Nombres[user]}")
        print(f"La maquina ha eligido {Nombres[pc]}")
    else:
        pass
    print("*" * 40)
    # SISTEMA DE ELECCION
    if user == pc:
        print("Empate")
    elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        PCVidas -= 1
        print("GANASTE")
    elif user not in range(1, 4):
        UserVidas -= 1
        print("Debes elegir dentro de 1-3 pierdes una vida")
    else:
        UserVidas -= 1
        print("PERDISTE")
    print("*" * 40)
    vidas = f"USUARIO VIDAS == {UserVidas}  MAQUINA VIDAS== {PCVidas}"
    print(vidas)
    # SISTEMA DE PUNTOS
    if UserVidas == 0:
        print("PERDISTE LA PARTIDA")
        break
    elif PCVidas == 0:
        print("GANASTE LA PARTIDA")
        break
