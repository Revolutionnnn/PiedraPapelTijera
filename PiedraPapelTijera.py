import random


def eleccion():
    pc = random.randint(1, 3)
    user = int(input("INGRESA UN NUMERO \n1 Piedra \n2 Papel \n3 Tijera \n"))
    Nombres = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera"
    }
    if user in Nombres:
        print(f"Haz elegido {Nombres[user]}")
        print(f"La maquina ha eligido {Nombres[pc]}")
    return user, pc


def reglas(user, pc, PCVidas, UserVidas):
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

    return PCVidas, UserVidas


def ganador(UserVidas, PCVidas):
    if UserVidas == 0:
        print("PERDISTE LA PARTIDA")
        exit()
    elif PCVidas == 0:
        print("GANASTE LA PARTIDA")
        exit()


def run():
    UserVidas = 3
    PCVidas = 3
    Round = 0

    while True:
        print("*" * 10)
        print(f"ROUND {Round}")
        print("*" * 10)
        Round += 1
        user, pc = eleccion()
        UserVidas, PCVidas = reglas(user, pc, UserVidas, PCVidas)
        ganador(UserVidas, PCVidas)


run()
