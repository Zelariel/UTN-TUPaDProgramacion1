# Variables iniciales

MAX_VIDA_JUGADOR = 100
vida_jugador = 100
vida_enemigo = 100
pociones = 3
turno_jugador = True
turnos_totales = 1
ATAQUE_PESADO = 15
GOLPE_CRITICO = ATAQUE_PESADO * 1.5
RAFAGA_VELOZ = 5
ATAQUE_ENEMIGO = 12

# Inicio

print("=========== BIENVENIDO A LA ARENA ===========\n")
nombre = input("Elija el nombre de su gladiador: ")

while not nombre.isalpha():
    print("\nError: Utilice solamente letras")
    nombre = input("\nIngrese un nombre: ")

print("\n=========== INICIO DEL COMBATE ===========")

while vida_jugador > 0 and vida_enemigo > 0:
    while turno_jugador:
        print(f"""\n=========== Turno {turnos_totales} Gladiador ===========
\nGladiador {nombre} (HP: {vida_jugador}) VS Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}""")
        print(f"""\nAcciones:
1) Ataque pesado
2) Ráfaga veloz
3) Usar poción\n""")
        accion = input("Elija un acción (1-3): ")
        while not accion.isdigit() or int(accion) < 1 or int(accion) > 3:
            print("Error: Ingrese solo números del 1 al 3")
            accion = input("Elija un acción (1-3): ")
        accion = int(accion)
        if accion == 1:
            if vida_enemigo < 20:
                print("\n>> Realizas un ataque pesado sobre el enemigo")
                print(">> ¡Golpe crítico! ¡Dañas al enemigo en " + "\033[1m" + str(GOLPE_CRITICO) + " puntos!" + "\033[0m")
                vida_enemigo -= GOLPE_CRITICO
                turnos_totales += 1
                turno_jugador = False
            else:
                print("\n>> Realizas un ataque pesado sobre el enemigo")
                print(">> Dañas al enemigo en " + "\033[1m" + str(ATAQUE_PESADO) + " puntos" + "\033[0m") # Número en cursiva
                vida_enemigo -= ATAQUE_PESADO
                turnos_totales += 1
                turno_jugador = False
        elif accion == 2:
            print("\n>> Realizas una ráfaga de golpes sobre el enemigo")
            for golpe in range(3):
                print(">> Golpe conectado por " + "\033[1m" + str(RAFAGA_VELOZ) + " puntos de daño" + "\033[0m")
                vida_enemigo -= RAFAGA_VELOZ
            turnos_totales += 1
            turno_jugador = False
        else:
            if pociones > 0:
                pociones -= 1
                vida_jugador += 30
                if vida_jugador > 100:
                    vida_jugador = MAX_VIDA_JUGADOR
                print("\n>> Tomas una poción de salud.")
                print(">> Recuperas " + "\033[1m" + "30 puntos" + "\033[0m" + f" de salud. (HP: {vida_jugador})")
                turnos_totales += 1
                turno_jugador = False
            else:
                print("\n>> ¡Te has quedado sin pociones!")
                print(">> ¡Has perdido la oportunidad de atacar!")
                turnos_totales += 1
                turno_jugador = False
    while not turno_jugador and vida_enemigo > 0:
        print("\n========== Turno Enemigo ===========")
        print("\n>> ¡El enemigo te ataca!")
        print(">> ¡Recibes " + "\033[1m" + str(ATAQUE_ENEMIGO) + " de daño!" + "\033[0m")
        vida_jugador -= ATAQUE_ENEMIGO
        turno_jugador = True

# Victoria o derrota

if vida_jugador <= 0:
    print("\n==================================================\n")
    print("\033[1m" + "========== ¡DERROTA! ==========" + "\033[0m")
    print(">> Has sido vencido en combate.\n")
elif vida_jugador > 0:
    print("\n==================================================\n")
    print("\033[1m" + "========== ¡VICTORIA! ==========" + "\033[0m")
    print(f">> ¡Felicitaciones {nombre}! ¡Has ganado el combate!\n")