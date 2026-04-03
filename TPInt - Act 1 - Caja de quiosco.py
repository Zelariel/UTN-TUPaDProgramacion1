print("---------- Caja del quiosco ----------\n")

# -------------------------------- Petición y validación del nombre del cliente --------------------------------

nombre = input("¡Bienvenido! Para empezar, ¿Cuál es su nombre?\n")

while nombre.isalpha() != True or len(nombre) == 0:
    nombre = input("Por favor, ingrese un nombre válido\n")

print("\n_______________________________________________________________________________\n")

# -------------------------------- Petición y validación de la cantidad de productos --------------------------------

cant_productos = input("¿Cuántos productos lleva?\n")

while cant_productos.isdigit() != True or int(cant_productos) <= 0:
    cant_productos = input("Por favor, ingrese una cantidad válida de productos\n")

cant_final = int(cant_productos)

print("\n_______________________________________________________________________________\n")

# -------------------------------- Petición y validación de datos de los productos --------------------------------

carrito = []
total_sin_desc= 0
total_con_desc = 0

for num_producto in range(1,cant_final+1):
    precio_producto = input(f"Ingrese el precio del {num_producto}° producto: ")
    
    while precio_producto.isdigit() != True or int(precio_producto) <= 0:
        precio_producto = input("Error, por favor ingrese el precio nuevamente: ")
        
    precio_final = float(precio_producto)
    
    tiene_descuento = input("¿El producto tiene descuento? (S/N): ").lower()

    bandera = True
    
    while bandera:
        if tiene_descuento == "s" or tiene_descuento == "n":
            bandera = False
        else:
            input("Por favor ingrese solamente S (si) o N (no): ")
    
    if tiene_descuento == "s":
        total_sin_desc += precio_final
        precio_final *= 0.9
        total_con_desc += precio_final        
    else:
        total_sin_desc += precio_final
        total_con_desc += precio_final
    
    carrito.append([num_producto,precio_final,tiene_descuento.upper()]) # Guardo info en listas

# -------------------------------- Salida en pantalla/consola --------------------------------

print("\n ////////////////////////////////////////////////////////////// \n")
print("Cliente:",nombre)
print("Cantidad de productos:",cant_final,"\n")

for num_producto in range(cant_final):
    print(f"Producto n° {carrito[num_producto][0]} - Precio: ${carrito[num_producto][1]} - Descuento: {carrito[num_producto][2]}")

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cant_final

print("\n")
print("Total sin descuentos: $",total_sin_desc)
print("Total con descuentos: $",total_con_desc)
print("Ahorro: $",ahorro)
print(f"Promedio por producto: ${promedio:.2f}")

print("\n")
print("¡Muchas gracias por comprar aquí! ¡Lo esperamos nuevamente!\n")