from tabulate import tabulate

#Almacen de listas
guias = []
paquetes = []
clientes = []
facturas = []
detalles_factura = []

def mostrar_tabla(datos, headers):
    """Función para mostrar forma de tabla."""
    if datos:
        print(tabulate(datos, headers=headers, tablefmt="grid"))
    else:
        print("No hay datos para mostrar.")

def crear_guia():
    codigo_guia = input("Ingrese el Código de la Guía: ")
    direccion_origen = input("Ingrese la Dirección de Origen: ")
    direccion_destino = input("Ingrese la Dirección de Destino: ")
    destinatario = input("Ingrese el Destinatario: ")
    guias.append([codigo_guia, direccion_origen, direccion_destino, destinatario])
    #Función para mostrar forma de tabla.
    mostrar_tabla(guias, ["Código de Guía", "Dirección de Origen", "Dirección de Destino", "Destinatario"])

def crear_paquete():
    codigo_paquete = input("Ingrese el Código del Paquete: ")
    peso = input("Ingrese el Peso: ")
    tipo = input("Ingrese el Tipo: ")
    descripcion = input("Ingrese la Descripción: ")
    paquetes.append([codigo_paquete, peso, tipo, descripcion])
    # Función para mostrar forma de tabla.
    mostrar_tabla(paquetes, ["Código de Paquete", "Peso", "Tipo", "Descripción"])

def crear_cliente():
    tipo_cliente = input("¿Es Cliente 1.Existente o 2.Nuevo? ")
    codigo_cliente = input("Ingrese el Código de Cliente: ")

    if tipo_cliente == '2':
        nit = input("Ingrese el NIT: ")
        nombre = input("Ingrese el Nombre: ")
        telefono = input("Ingrese el Teléfono: ")
        direccion = input("Ingrese la Dirección: ")
        dpi = input("Ingrese el DPI: ")
        email = input("Ingrese el Email: ")
        clientes.append([codigo_cliente, nit, nombre, telefono, direccion, dpi, email])
        # Función para mostrar forma de tabla.
        mostrar_tabla(clientes, ["Código de Cliente", "NIT", "Nombre", "Teléfono", "Dirección", "DPI", "Email"])
    else:
        # Función para mostrar forma de tabla.
        mostrar_tabla(clientes, ["Código de Cliente", "NIT", "Nombre", "Teléfono", "Dirección", "DPI", "Email"])

def crear_factura():
    codigo_factura = input("Ingrese el Código de la Factura: ")
    tipo_pago = input("Ingrese el Tipo de Pago: ")
    codigo_guia = input("Ingrese el Código de la Guía: ")
    codigo_cliente = input("Ingrese el Código del Cliente: ")
    codigo_empleado = input("Ingrese el Código del Empleado: ")
    facturas.append([codigo_factura, tipo_pago, codigo_guia, codigo_cliente, codigo_empleado])
    # Función para mostrar forma de tabla.
    mostrar_tabla(facturas, ["Código de Factura", "Tipo de Pago", "Código de Guía", "Código de Cliente", "Código de Empleado"])

def crear_detalle_factura():
    codigo_detalle = input("Ingrese el Código de Detalle: ")
    codigo_factura = input("Ingrese el Código de la Factura: ")
    codigo_paquete = input("Ingrese el Código del Paquete: ")
    fecha_envio = input("Ingrese la Fecha de Envío: ")
    detalles_factura.append([codigo_detalle, codigo_factura, codigo_paquete, fecha_envio])
    # Función para mostrar forma de tabla.
    mostrar_tabla(detalles_factura, ["Código Detalle", "Código Factura", "Código Paquete", "Fecha de Envío"])

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Guía")
        print("2. Paquete")
        print("3. Cliente")
        print("4. Factura")
        print("5. Detalle Factura")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            submenu("Guía", crear_guia)
        elif opcion == '2':
            submenu("Paquete", crear_paquete)
        elif opcion == '3':
            submenu("Cliente", crear_cliente)
        elif opcion == '4':
            submenu("Factura", crear_factura)
        elif opcion == '5':
            submenu("Detalle Factura", crear_detalle_factura)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def submenu(entidad, crear_funcion):
    while True:
        print(f"\n--- Menú {entidad} ---")
        print("1. Crear")
        print("2. Eliminar")
        print("3. Actualizar")
        print("4. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_funcion()
        elif opcion == '2':
            eliminar_funcion(entidad)
        elif opcion == '3':
            actualizar_funcion(entidad)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def eliminar_funcion(entidad):
    print(f"Eliminar {entidad}: Función no implementada aún.")

def actualizar_funcion(entidad):
    print(f"Actualizar {entidad}: Función no implementada aún.")

# Ejecutar el menú principal
menu_principal()
