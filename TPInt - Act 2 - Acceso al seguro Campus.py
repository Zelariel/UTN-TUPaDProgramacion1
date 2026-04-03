usuario_correcto = "Jorge123"
password_correcta = "prog2026"
intentos = 0
INTENTOS_MAX = 3

print("---------- ¡Bienvenido al Campus! ---------\n")
print("------------------ Ingreso ------------------\n")

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

while usuario != usuario_correcto or password != password_correcta:
    intentos += 1
    if intentos < 3:
        print(f"""\nIntento {intentos}/{INTENTOS_MAX}:\n
> Usuario: {usuario}
> Contraseña: {password}\n
Error: Credenciales inválidas. Intente nuevamente.\n""")
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
    else:
        print(f"""\nIntento {intentos}/{INTENTOS_MAX}:\n
> Usuario: {usuario}
> Contraseña: {password}\n
Error: Credenciales inválidas. Cuenta Bloqueada.\n""")
        break

if usuario == usuario_correcto and password == password_correcta: print(f"\n¡Bienvenido {usuario}!\n")

while usuario == usuario_correcto and password == password_correcta:
    print("""Menú:\n
1) Ver estado de inscripción
2) Cambiar contraseña
3) Mostrar mensaje motivacional
4) Salir""")
    
    opcion = input("Ingrese una opción (1-4): ")
    
    while opcion.isdigit() == False:
        print("Error: Por favor ingrese un número")
        opcion = input("Ingrese una opción (1-4): ")
        
    while int(opcion) < 1 or int(opcion) > 4:
        print("Error: Fuera de rango. Por favor ingrese un número del 1 al 4")
        opcion = input("Ingrese una opción (1-4): ")
        
    opcion_num = int(opcion)
        
    if opcion_num == 1:
        print("\n> Estado de inscripción: Inscripto\n")
    elif opcion_num == 2:
        cambio_pass = input("\n¿Desea cambiar su contraseña? S/N: ").lower()
        checkpoint_1 = True
        while checkpoint_1:
            if cambio_pass == "n":
                checkpoint_1 = False
            elif cambio_pass == "s":
                new_pass = input("Ingrese una nueva contraseña: ")
                while len(new_pass) < 6:
                    print("La contraseña debe tener 6 caracteres como mínimo.")
                    new_pass = input("Por favor, ingrese una nueva contraseña: ")
                while new_pass == password_correcta:
                    print("La contraseña es la misma que la actual.")
                    new_pass = input("Por favor, ingrese una nueva contraseña: ")
                new_pass_repeat = input("Por favor confirme nuevamente la nueva contraseña: ")
                while new_pass != new_pass_repeat:
                    print("Error: Las contraseñas no coinciden")
                    new_pass = input("Ingrese una nueva contraseña: ")
                    new_pass_repeat = input("Ingrese nuevamente la contraseña: ")
                confirmar_cambio = input("\n¿Desea confirmar el cambio de contraseña? S/N: ").lower()
                checkpoint_2 = True
                while checkpoint_2:
                    if confirmar_cambio == "n":
                        checkpoint_2 = False
                    elif confirmar_cambio == "s":
                        password_correcta = new_pass
                        password = password_correcta
                        print("\nCambio realizado con éxito\n")
                        checkpoint_2 = False
                    else:
                        confirmar_cambio = input("Error: Responda con S (si) o N (no): ").lower()
                checkpoint_1 = False
            else:
                cambio_pass = input("Error: Responda con S (si) o N (no): ").lower()
    elif opcion_num == 3:
        print("\n>> ¡¡Sigue practicando!! ¡¡Vas muy bien!! <<\n")
    elif opcion_num == 4:
        print("\nSaliendo de la app...\n")
        break