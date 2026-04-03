#Variables inciales

MAX_ENERGIA = 100
energia = 100
MAX_INTENTOS_FORZ_CERR = 3
intentos_forz_cerr = 0
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#Inicio

print("¡Bienvenido al desafío de abrir la bóveda!\n")
nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("\nError: Utilice solamente letras")
    nombre = input("\nIngrese su nombre: ")

while (energia > 0 and tiempo > 0 and cerraduras_abiertas < 3) and alarma == False:
    print(f"""\nAgente {nombre}:
Energía: {energia}
Tiempo: {tiempo}
Cerraduras abiertas: {cerraduras_abiertas}\n""")
    print("""Acciones:
1) Forzar cerradura (Costo: -20 energía, -2 tiempo)
2) Hackear panel (Costo: -10 energía, -3 tiempo)
3) Descansar (Costo: +15 energía, -1 tiempo)\n""")
    accion = input("Elija una acción: ")
    while not accion.isdigit() or int(accion) < 1 or int(accion) > 3:
        print("Error: Use solamente números del 1 al 3.")
        accion = input("Elija una acción: ")
    accion = int(accion)
    
# Forzar Cerraduras

    if accion == 1:
        numero = input("\nElija un número del 1 al 3: ")
        while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
            print("Error: Use solamente números del 1 al 3.")
            numero = input("\nElija un número del 1 al 3: ")
        numero = int(numero)
        if energia < 40:                
            if numero == 1 or numero == 2:
                intentos_forz_cerr += 1
                if intentos_forz_cerr == MAX_INTENTOS_FORZ_CERR:
                    energia -= 20 # Valor base 20
                    tiempo -= 2 # Valor base 2
                    print("\nHas fallado y ha saltado la alarma.")
                    print("El sistema se ha bloqueado.")
                    alarma = True
                else:
                    energia -= 20 # Valor base 20
                    tiempo -= 2 # Valor base 2
                    cerraduras_abiertas += 1
                    print("\nHas forzado la cerradura con éxito.")
            else:
                energia -= 20 # Valor base 20
                tiempo -= 2 # Valor base 2
                print("\nHas fallado y ha saltado la alarma.")
                print("El sistema se ha bloqueado.")
                alarma = True
        else:
            intentos_forz_cerr += 1
            if intentos_forz_cerr == MAX_INTENTOS_FORZ_CERR:
                energia -= 20 # Valor base 20
                tiempo -= 2 # Valor base 2
                print("\nHas fallado y ha saltado la alarma.")
                print("El sistema se ha bloqueado.")
                alarma = True
            else:
                energia -= 20 # Valor base 20
                tiempo -= 2 # Valor base 2
                cerraduras_abiertas += 1
                print("\nHas forzado la cerradura con éxito.")

# Hackear Panel

    elif accion == 2:
        intentos_forz_cerr = 0
        energia -= 10
        tiempo -= 3
        for x in range(4):
            codigo_parcial += "x"
        print("\nHackeando panel...")
        if len(codigo_parcial) == 4:
            print("\nHackeado 50%")
        elif len(codigo_parcial) == 8:
            print("\nHackeo completo.")
            cerraduras_abiertas += 1
            codigo_parcial = ""

# Descansar

    else:
        intentos_forz_cerr = 0
        if alarma == True:
            energia += 5
            tiempo -=1
            print("Has descansado poco por el ruido de la alarma.")
        else:
            energia += 15
            tiempo -=1
            print("Has descansado.")
        if energia > MAX_ENERGIA:
                energia = MAX_ENERGIA

# Fin del juego

if alarma == True:
    print("\nBloqueado por alarma. Fin del juego.\n")
elif tiempo <= 0 and energia <= 0:
    print("\nTe has quedado sin tiempo ni energía. Fin del juego.\n")
elif energia <= 0 and tiempo > 0:
    print("\nTe has quedado sin energía. Fin del juego.\n")
elif tiempo <= 0 and energia > 0:
    print("\nTe has quedado sin tiempo. Fin del juego.\n")
elif cerraduras_abiertas == 3:
    print("\n¡Lo has logrado! ¡Felicitaciones!\n")