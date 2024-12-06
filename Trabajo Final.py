# Variables globales
# La variable precios almacena el costo de las entradas para cada sala en las categorias VIP y General.
precios = [[0, 0], [0, 0], [0, 0]]  # [VIP, General] para cada sala

# Lista que almacena los nombres de las peliculas creadas.
peliculas = []

# Lista que almacena la asignacion de una pelicula a cada sala.
asignaciones = ["", "", ""]

# Listas que representan los asientos disponibles en cada sala.
sala1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sala2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sala3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Lista que almacena las facturas generadas durante la venta de boletos.
facturas = []

# Lista que almacena el ingreso total acumulado para cada sala.
cuadre = [0, 0, 0]  # Total por sala

def menu():
    # Menu principal del programa
    while True:
        print("\nMenu Cinema")
        print(" 1. Precios de Sala")
        print(" 2. Crear pelicula")
        print(" 3. Asignar pelicula a sala")
        print(" 4. Vender tiquetes")
        print(" 5. Buscar Factura")
        print(" 6. Mostrar Salas")
        print(" 7. Cuadre de caja")
        print(" 8. Salir")

        # Solicitar al usuario que seleccione una opcion
        opc = int(input("\nDigite una opcion: "))

        # Llamar a la funcion correspondiente segun la opcion seleccionada
        if opc == 1:
            print("\nPrecios de Sala:")
            menu_precios_sala()
        elif opc == 2:
            print("\nCrear Pelicula:")
            crear_pelicula()
        elif opc == 3:
            print("\nAsignar Pelicula a Sala:")
            asignar_pelicula()
        elif opc == 4:
            print("\nVender Tiquetes:")
            vender_tiquetes()
        elif opc == 5:
            print("\nBuscar Factura:")
            buscar_factura()
        elif opc == 6:
            print("\nMostrar Salas:")
            mostrar_salas()
        elif opc == 7:
            print("\nCuadre de Caja:")
            cuadre_caja()
            # Manejar la salida
        elif opc == 8:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion invalida. Intente nuevamente.")



def menu_precios_sala():
    # Menu para configurar los precios de las salas
    print("\nMenu Precios de Sala")
    print(" 1. Sala 1")
    print(" 2. Sala 2")
    print(" 3. Sala 3")
    print(" 4. Volver al Menu Principal")

    # Solicitar al usuario que seleccione una sala
    opc = int(input("\nDigite una opcion: "))

    # Actualizar los precios de la sala seleccionada
    if opc == 1 or opc == 2 or opc == 3:
        precios[opc - 1][0] = int(input("Ingrese el valor de la silla VIP: "))
        precios[opc - 1][1] = int(input("Ingrese el valor de la silla General: "))
        menu_precios_sala()
    elif opc == 4:
        return
    else:
        print("Ingrese una opcion valida")
        menu_precios_sala()

def crear_pelicula():
    # Crear una nueva pelicula
    nombre = input("Digite el nombre de la pelicula: ")
    peliculas.append(nombre)
    print(f"La pelicula {nombre} se registro con el codigo {len(peliculas)}")

    # Preguntar si el usuario desea registrar otra pelicula
    continuar = input("Desea crear otra pelicula? (si/no): ")
    if continuar.lower() == "si":
        crear_pelicula()
    else:
        menu()

def asignar_pelicula():
    # Asignar una pelicula a una sala
    sala = int(input("Digite el numero de la Sala (1-3): ")) - 1
    codigo = int(input("Digite el codigo de la pelicula: ")) - 1
    if 0 <= sala <= 2 and 0 <= codigo < len(peliculas):
        asignaciones[sala] = peliculas[codigo]
        print(f"La pelicula {peliculas[codigo]} ha sido registrada a la Sala {sala + 1}")
    else:
        print("Sala o codigo de pelicula invalidos.")

    # Preguntar si el usuario desea asignar otra pelicula
    continuar = input("Desea asignar otra pelicula a alguna sala? (si/no): ")
    if continuar.lower() == "si":
        asignar_pelicula()
    else:
        return

def mostrar_sala(sala):
    # Mostrar el estado actual de una sala en filas de 5 asientos
    for i in range(0, len(sala), 5):
        fila = ""
        for j in range(i, i + 5):
            if j < len(sala):
                fila += f"{sala[j]} " if sala[j] != "X" else "X "
        print(fila)

def vender_tiquetes():
    # Funcion para vender tiquetes de una pelicula asignada a una sala
    print("\nSeleccione la pelicula:")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}. {pelicula}")

    pelicula_seleccionada = int(input("Digite una opcion: ")) - 1

    # Validar que la pelicula seleccionada exista
    if 0 <= pelicula_seleccionada < len(peliculas):
        sala = -1
        for i in range(3):
            if asignaciones[i] == peliculas[pelicula_seleccionada]:
                sala = i
                break

        if sala != -1:
            # Gestion de las ventas de boletos para la sala asignada
            salas = [sala1, sala2, sala3]
            precios_sala = precios[sala]
            sillas_vip = []
            sillas_general = []
            total_vip = 0
            total_general = 0

            print(f"\nLa pelicula {peliculas[pelicula_seleccionada]} esta asignada a la Sala {sala + 1}")
            while True:
                print("\nEstado actual de la sala:")
                mostrar_sala(salas[sala])

                # Solicitar al usuario que seleccione un asiento
                silla = int(input("\nSeleccione la silla: ")) - 1
                if 0 <= silla < len(salas[sala]):
                    if salas[sala][silla] != "X":
                        tipo_silla = "VIP" if (sala == 0 and silla < 5) or (sala == 1 and silla < 10) else "General"
                        if tipo_silla == "VIP":
                            sillas_vip.append(silla + 1)
                            total_vip += precios_sala[0]
                        else:
                            sillas_general.append(silla + 1)
                            total_general += precios_sala[1]
                        salas[sala][silla] = "X"
                        print(f"La silla {silla + 1} es {tipo_silla}, esta disponible.")
                    else:
                        print("La silla no esta disponible.")
                else:
                    print("Silla invalida.")

                # Preguntar si el usuario desea comprar otra silla
                continuar = input("Desea comprar otra silla? (si/no): ")
                if continuar.lower() == "no":
                    comprador = input("Digite su nombre: ")
                    factura = {
                        "id": len(facturas) + 1,
                        "pelicula": peliculas[pelicula_seleccionada],
                        "sala": sala + 1,
                        "nombre": comprador,
                        "sillas_vip": sillas_vip,
                        "sillas_general": sillas_general,
                        "total_vip": total_vip,
                        "total_general": total_general,
                        "total": total_vip + total_general,
                    }
                    facturas.append(factura)
                    cuadre[sala] += total_vip + total_general

                    print("\n—------------------")
                    print(f"Factura No: {factura['id']}")
                    print(f"Pelicula: {factura['pelicula']}")
                    print(f"Sala: {factura['sala']}")
                    print(f"Nombre: {factura['nombre']}")
                    print(f"Numero de sillas: {len(sillas_vip) + len(sillas_general)}")
                    print("Sillas VIP: ", end="")
                    if sillas_vip:
                        for silla in sillas_vip:
                            print(silla, end=" ")
                    else:
                        print("Ninguna")
                    print("\nSillas General: ", end="")
                    if sillas_general:
                        for silla in sillas_general:
                            print(silla, end=" ")
                    else:
                        print("Ninguna")
                    print(f"\nValor sillas VIP: {total_vip}")
                    print(f"Valor sillas general: {total_general}")
                    print(f"Total a pagar : {factura['total']}")
                    print("—------------------")
                    return
        else:
            print("Pelicula no asignada a ninguna sala.")
    else:
        print("Opcion invalida.")
    return

def buscar_factura():
    # Buscar y mostrar informacion de una factura especifica
    while True:
        numero = int(input("Digite el Numero de la Factura: "))
        encontrada = False
        for factura in facturas:
            if factura["id"] == numero:
                encontrada = True
                print("\n—------------------")
                print(f"Factura No: {factura['id']}")
                print(f"Pelicula: {factura['pelicula']}")
                print(f"Sala: {factura['sala']}")
                print(f"Nombre: {factura['nombre']}")
                print(f"Numero de sillas: {len(factura['sillas_vip']) + len(factura['sillas_general'])}")
                print("Sillas VIP: ", end="")
                if factura["sillas_vip"]:
                    for silla in factura["sillas_vip"]:
                        print(silla, end=" ")
                else:
                    print("Ninguna")
                print("\nSillas General: ", end="")
                if factura["sillas_general"]:
                    for silla in factura["sillas_general"]:
                        print(silla, end=" ")
                else:
                    print("Ninguna")
                print(f"\nValor sillas VIP: {factura['total_vip']}")
                print(f"Valor sillas general: {factura['total_general']}")
                print(f"Total a pagar : {factura['total']}")
                print("—------------------")
                break
            else:
                encontrada = False
                break
        if encontrada == False:
            print("La Factura no existe")
        continuar = input("Desea buscar otra factura, si o no: ")
        if continuar != "si":
            return


def cuadre_caja():
    # Mostrar el ingreso total por sala o general
    print("\nCuadre de caja")
    print(" 1. Cuadre por Sala")
    print(" 2. Cuadre General")

    opc = int(input("\nDigite una opcion: "))

    if opc == 1:
        sala = int(input("Digite el numero de la Sala (1-3): ")) - 1
        if 0 <= sala < 3:
            if asignaciones[sala]:
                print(f"\nPelicula: {asignaciones[sala]}")
            else:
                print("Sala sin asignar.")
            print(f"Total Sala {sala + 1}: {cuadre[sala]}")
        else:
            print("Sala invalida.")
        return
    elif opc == 2:
        total_general = cuadre[0] + cuadre[1] + cuadre [2]
        print(f"\nTotal general de todas las salas: {total_general}")
        return
    else:
        print("Opcion invalida")
        cuadre_caja()

def mostrar_salas():
    # Mostrar el estado actual de todas las salas
    print("\nEstado de las Salas")
    salas = [sala1, sala2, sala3]
    for i, sala in enumerate(salas):
        print(f"\nSala {i + 1}: ", end="")
        if asignaciones[i] == "":
            print("Sin asignar")
        else:
            print(asignaciones[i])
        mostrar_sala(sala)
    return

# Iniciar el programa
menu()