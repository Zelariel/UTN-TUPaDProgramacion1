#Variables principales

lunes_1 = ""
lunes_2 = "Marcos"
lunes_3 = ""
lunes_4 = "Maria"

martes_1 = "Marcela"
martes_2 = "Juan"
martes_3 = ""

#Programa

operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    operador = input("Por favor utilice solo letas. ingrese su nombre: ")

print("""¡Bienvenido al turnero!
Por favor complete todos los datos del registro:\n""")

while operador.isalpha():
    print("""\nMenú:\n
1) Reservar turno (con nombre)
2) Cancelar turno (con nombre)
3) Ver agenda del día
4) Ver resumen general
5) Cerrar sistema\n""")

    opcion = input("Ingrese una opción (1-5): ")

    while not opcion.isdigit():
        print("Error: Por favor ingrese un número")
        opcion = input("Ingrese una opción (1-5): ")

    while int(opcion) < 1 or int(opcion) > 5:
        print("Error: Fuera de rango. Por favor ingrese un número del 1 al 5")
        opcion = input("Ingrese una opción (1-5): ")

    opcion_num = int(opcion)

#Agendar turno

    if opcion_num == 1:
        print("Elija el día: ")
        dia = input("1) Lunes | 2) Martes: ")
        while not dia.isdigit() or (int(dia) < 1 or int(dia) > 2):
            dia = input("Por favor, utilice 1 (lunes) o 2 (martes) para responder: ")
        
        dia = int(dia)
        paciente = input("Ingrese nombre del paciente: ")
        
        while not paciente.isalpha():
            paciente = input("Por favor, utilice solamente letras: ")
        
        if dia == 1:
            if paciente in [lunes_1,lunes_2,lunes_3,lunes_4]:
                print("\nEl paciente ya tiene turno agendado el lunes.\n")
            else:
                if lunes_1 == "" or lunes_1 == "(libre)":
                    lunes_1 = paciente
                    print("\nTurno agendado con éxito.\n")
                elif lunes_2 == "" or lunes_2 == "(libre)":
                    lunes_2 = paciente
                    print("\nTurno agendado con éxito.\n")
                elif lunes_3 == "" or lunes_3 == "(libre)":
                    lunes_3 = paciente
                    print("\nTurno agendado con éxito.\n")
                elif lunes_4 == "" or lunes_4 == "(libre)":
                    lunes_4 = paciente
                    print("\nTurno agendado con éxito.\n")
                else:
                    print("\nNo quedan turnos disponibles el lunes.\n")
        else:
            if paciente in [martes_1,martes_2,martes_3]:
                print("\nEl paciente ya tiene turno agendado el martes.\n")
            else:
                if martes_1 == "" or martes_1 == "(libre)":
                    martes_1 = paciente
                    print("\nTurno agendado con éxito.\n")
                elif martes_2 == "" or martes_2 == "(libre)":
                    martes_2 = paciente
                    print("\nTurno agendado con éxito.\n")
                elif martes_3 == "" or martes_3 == "(libre)":
                    martes_3 = paciente
                    print("\nTurno agendado con éxito.\n")
                else:
                    print("\nNo quedan turnos disponibles el martes.\n")

# Cancelar turno

    elif opcion_num == 2:
        print("Elija el día: ")
        dia = input("1) Lunes | 2) Martes: ")
        while not dia.isdigit() or (int(dia) < 1 or int(dia) > 2):
            dia = input("Por favor, utilice 1 (lunes) o 2 (martes) para responder: ")
            
        dia = int(dia)
        paciente = input("Ingrese nombre del paciente: ")
        
        while not paciente.isalpha():
            paciente = input("Por favor, utilice solamente letras: ")
        
        if dia == 1:
            if paciente not in [lunes_1,lunes_2,lunes_3,lunes_4]:
                print("\nEl paciente no tiene turno agendado el lunes.\n")
            else:
                if lunes_1 == paciente:
                    lunes_1 = ""
                    print("\nTurno eliminado con éxito.\n")
                elif lunes_2 == paciente:
                    lunes_2 = ""
                    print("\nTurno eliminado con éxito.\n")
                elif lunes_3 == paciente:
                    lunes_3 = ""
                    print("\nTurno eliminado con éxito.\n")
                elif lunes_4 == paciente:
                    lunes_4 = ""
                    print("\nTurno eliminado con éxito.\n")
                else:
                    print("\nPaciente no encontrado.\n")
        else:
            if paciente not in [martes_1,martes_2,martes_3]:
                print("\nEl paciente no tiene turno agendado el martes.\n")
            else:
                if martes_1 == paciente:
                    martes_1 = ""
                    print("\nTurno eliminado con éxito.\n")
                elif martes_2 == paciente:
                    martes_2 = ""
                    print("\nTurno eliminado con éxito.\n")
                elif martes_3 == paciente:
                    martes_3 = ""
                    print("\nTurno eliminado con éxito.\n")
                else:
                    print("\nPaciente no encontrado.\n")

#Agenda diaria

    elif opcion_num == 3:
        print("Elija el día: ")
        dia = input("1) Lunes | 2) Martes: ")

        while not dia.isdigit() or (int(dia) < 1 or int(dia) > 2):
            dia = input("Por favor, utilice 1 (lunes) o 2 (martes) para responder: ")

        dia = int(dia)

        if lunes_1 == "":
            lunes_1 = "(libre)"
        if lunes_2 == "":
            lunes_2 = "(libre)"
        if lunes_3 == "":
            lunes_3 = "(libre)"
        if lunes_4 == "":
            lunes_4 = "(libre)"
        
        if martes_1 == "":
            martes_1 = "(libre)"
        if martes_2 == "":
            martes_2 = "(libre)"
        if martes_3 == "":
            martes_3 = "(libre)"

        if dia == 1:
            print(f"""\nAgenda del lunes:
Turno 1: {lunes_1}
Turno 2: {lunes_2}
Turno 3: {lunes_3}
Turno 4: {lunes_4}\n""")
        else:
            print(f"""\nAgenda del martes:
Turno 1: {martes_1}
Turno 2: {martes_2}
Turno 3: {martes_3}\n""")

#Resumen

    elif opcion_num == 4:
        MAX_TURNOS_LUNES = 4
        MAX_TURNOS_MARTES = 3
        ocupados_lunes = 0
        ocupados_martes = 0

        ocupados_lunes = sum([(lunes_1 != "" and lunes_1 != "(libre)"), (lunes_2 != "" and lunes_2 != "(libre)"), (lunes_3 != "" and lunes_3 != "(libre)"), (lunes_4 != "" and lunes_4 != "(libre)")])
        ocupados_martes = sum([(martes_1 != "" and martes_1 != "(libre)"), (martes_2 != "" and martes_2 != "(libre)"), (martes_3 != "" and martes_3 != "(libre)")])

        print(f"\nTurnos lunes: {ocupados_lunes} ocupados / {MAX_TURNOS_LUNES - ocupados_lunes} libres.")
        print(f"\nTurnos martes: {ocupados_martes} ocupados / {MAX_TURNOS_MARTES - ocupados_martes} libres.")
        
        if ocupados_lunes > ocupados_martes:
            print("\nEl día con más turnos es el lunes.")
        elif ocupados_lunes < ocupados_martes:
            print("\nEl día con más tunrnos es el martes.")
        else:
            print("\nEmpate. Ambos días tienen la misma cantidad de turnos agendados.")

#Salir del sistema

    elif opcion_num == 5:
        print("\nSistema cerrado.\n")
        break
