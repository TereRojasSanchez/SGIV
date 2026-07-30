from dao.cliente_dao import ClienteDAO
from models.cliente import Cliente
from dao.mascota_dao import MascotaDAO
from models.mascota import Mascota
from dao.tratamiento_dao import TratamientoDAO
from models.tratamiento import Tratamiento
from dao.empleado_dao import EmpleadoDAO
from models.empleado import Empleado
from dao.ventas_dao import Ventas
from models.ventas import Ventas


def ver_clientes():
    try:
        cliente_dao = ClienteDAO()
        lista = cliente_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay clientes registrados")
        else:
            for cliente in lista:
                print(f"id: {cliente.id} {cliente.nombre} {cliente.apellido_paterno} {cliente.apellido_materno} {cliente.telefono} {cliente.correo} {cliente.calle} {cliente.no_exterior} {cliente.no_interior}{cliente.colonia} {cliente.municipio} {cliente.codigo_postal}")
        print("\n Conexion exitosa con la base de datos")

    except Exception as e:
        print("Error")
        print(e)


def insertar_cliente():
    print("INSERTAR UN NUEVO CLIENTE")
    nombre = input("Escribe el nombre: ")
    apellido_paterno = input("Escribe el apellido paterno: ")
    apellido_materno = input("Escribe el apellido materno: ")
    telefono = input("Escribe el número telefónico: ")
    correo = input("Escribe el correo: ")
    calle = input("Escribe la calle donde vive: ")
    no_exterior = input("Escribe el número exterior: ")
    no_interior = input("Escribe el numero interior:")
    colonia = input("Escribe la colonia: ")
    municipio = input("Escribe el municipio donde vive: ")
    codigo_postal = input("Escribe el código postal: ")

    try:
        cliente_dao = ClienteDAO()

        cliente = Cliente(
            None,
            nombre,
            apellido_paterno,
            apellido_materno,
            telefono,
            correo,
            calle,
            no_exterior,
            no_interior,
            colonia,
            municipio,
            codigo_postal
        )

        cliente_dao.insertar(cliente)

        print("Insercion del nuevo cliente fue exitosa")

    except Exception as e:
        print("Error al insertar el cliente")
        print(e)

def actualizar_cliente():
    try:
        cliente_dao = ClienteDAO()
        print("Lista de clientes disponibles")
        lista = cliente_dao.obtener_todo()

        for cliente in lista:
            print(f"ID: {cliente.id} - Nombre: {cliente.nombre}")

        print("")
        id = int(input("Seleccione el id del cliente a actualizar: "))
        nombre = input("Escribe el nombre: ")
        apellido_paterno = input("Escribe el apellido paterno: ")
        apellido_materno = input("Escribe el apellido materno: ")
        telefono = input("Escribe el telefono: ")
        correo = input("Escribe el correo: ")
        calle = input("Escribe la calle: ")
        no_exterior = input("Escribe el numero exterior: ")
        no_interior = input("Escribe el numero interior:")
        colonia = input("Escribe la colonia: ")
        municipio = input("Escribe el municipio: ")
        codigo_postal = input("Escribe el codigo postal: ")

        cliente = Cliente(
            id,
            nombre,
            apellido_paterno,
            apellido_materno,
            telefono,
            correo,
            calle,
            no_exterior,
            no_interior,
            colonia,
            municipio,
            codigo_postal
        )

        cliente_dao.actualizar(cliente)
        print("El cliente fue actualizado con éxito")

    except Exception as e:
        print("ERROR al actualizar el cliente")
        print(e) 

def eliminar_cliente():
    try:
        cliente_dao = ClienteDAO()
        print("Lista de clientes disponibles")

        lista = cliente_dao.obtener_todo()

        for cliente in lista:
            print(f"ID: {cliente.id} - Nombre: {cliente.nombre}")

        id = int(input("Escriba el id del cliente a eliminar: "))

        cliente_dao.eliminar(id)

        print(f"El cliente {id} ha sido eliminado con éxito")

    except Exception as e:
        print("Error al eliminar el cliente")
        print(e)

def menu_clientes():
    print("1. Ver todos los clientes")
    print("2. Insertar un nuevo cliente")
    print("3. Actualizar un cliente existente")
    print("4. Eliminar un cliente existente")
    opcion = int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_clientes()
        case 2:
            insertar_cliente()
        case 3:
            actualizar_cliente()
        case 4:
            eliminar_cliente()



# MASCOTAS

def ver_mascotas():
    try:
        mascota_dao = MascotaDAO()
        lista = mascota_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay mascotas registradas")
        else:
            for mascota in lista:
                print(
                    f"ID: {mascota.id} "
                    f"ID Cliente: {mascota.id_cliente} "
                    f"Nombre: {mascota.nombre} "
                    f"Raza: {mascota.raza} "
                    f"Especie: {mascota.especie}  "
                    f"Edad: {mascota.edad}  "
                    f"Peso: {mascota.peso}"
                )

        print("\nConexión exitosa con la base de datos")

    except Exception as e:
        print("Error")
        print(e)


def insertar_mascota():
    print("\nINSERTAR UNA NUEVA MASCOTA")

    id_cliente = int(input("Escribe el ID del cliente: "))
    nombre = input("Escribe el nombre de la mascota: ")
    raza = input("Escribe la raza: ")
    especie = input("Escribe la especie: ")
    edad = int(input("Escribe la edad: "))
    peso = float(input("Escribe el peso: "))

    try:
        mascota_dao = MascotaDAO()

        mascota = Mascota(
            None,
            id_cliente,
            nombre,
            raza,
            especie,
            edad,
            peso
        )

        mascota_dao.insertar(mascota)

        print("La mascota fue registrada con éxito")

    except Exception as e:
        print("Error al insertar la mascota")
        print(e)


def actualizar_mascota():
    try:
        mascota_dao = MascotaDAO()

        print("\nLista de mascotas")

        lista = mascota_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay mascotas registradas.")
            return

        for mascota in lista:
            print(f"ID: {mascota.id} - {mascota.nombre}")

        id = int(input("\nSeleccione el ID de la mascota: "))
        id_cliente = int(input("Escribe el ID del cliente: "))
        nombre = input("Nuevo nombre: ")
        raza = input("Nueva raza: ")
        especie = input("Nueva especie: ")
        edad = int(input("Nueva edad: "))
        peso = float(input("Nuevo peso: "))

        mascota = Mascota(
            id,
            id_cliente,
            nombre,
            raza,
            especie,
            edad,
            peso
        )

        mascota_dao.actualizar(mascota)

        print("La mascota fue actualizada correctamente.")

    except Exception as e:
        print("Error al actualizar la mascota")
        print(e)


def eliminar_mascota():
    try:
        mascota_dao = MascotaDAO()

        print("\nLista de mascotas")

        lista = mascota_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay mascotas registradas.")
            return

        for mascota in lista:
            print(f"ID: {mascota.id} - {mascota.nombre}")

        id = int(input("\nEscriba el ID de la mascota a eliminar: "))

        mascota_dao.eliminar(id)

        print("La mascota fue eliminada correctamente.")

    except Exception as e:
        print("Error al eliminar la mascota")
        print(e)


def menu_mascotas():
    while True:
        print("\n===== MENÚ MASCOTAS =====")
        print("1. Ver todas las mascotas")
        print("2. Insertar mascota")
        print("3. Actualizar mascota")
        print("4. Eliminar mascota")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                ver_mascotas()
            case "2":
                insertar_mascota()
            case "3":
                actualizar_mascota()
            case "4":
                eliminar_mascota()
            case "5":
                break
            case _:
                print("Opción inválida")

def menu_principal():
    while True:
        print("\n===== SISTEMA VETERINARIA =====")
        print("1. Clientes")
        print("2. Mascotas")
        print("3. Tratamiento")
        print("4. Empleado")
        print("5. Ventas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                menu_clientes()
            case "2":
                menu_mascotas()
            case "3":
                menu_tratamientos()
            case "4":
                menu_empleados()
            case "5":
                menu_ventas()
            case "6":
                print("Gracias por utilizar el sistema.")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")






# TRATAMIENTO


def ver_tratamiento():
    try:
        tratamiento_dao = TratamientoDAO()
        lista = tratamiento_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay tratamientos registrados.")
        else:
            print("\n===== LISTA DE TRATAMIENTOS =====")
            for t in lista:
                print(
                    f"ID: {t.id}  "
                    f"Medicamento: {t.medicamento}  "
                    f"Dosis: {t.dosis}  "
                    f"Fecha inicio: {t.fecha_inicio}  "
                    f"Fecha fin: {t.fecha_fin}  "
                    f"Indicaciones: {t.indicacion} "
                    f"ID Consulta: {t.id_consulta}"
                )

    except Exception as e:
        print("Error al consultar tratamientos:")
        print(e)

def insertar_tratamiento():
    try:
        print("\n===== INSERTAR TRATAMIENTO =====")

        id_consulta = int(input("ID de la consulta: "))
        medicamento = input("Medicamento: ")
        dosis = input("Dosis: ")
        fecha_inicio = input("Fecha inicio (AAAA-MM-DD): ")
        fecha_fin = input("Fecha fin (AAAA-MM-DD): ")
        indicacion = input("Indicaciones: ")

        tratamiento = Tratamiento(
            None,
            medicamento,
            dosis,
            fecha_inicio,
            fecha_fin,
            indicacion,
            id_consulta
        )

        tratamiento_dao = TratamientoDAO()
        tratamiento_dao.insertar(tratamiento)

        print("\nTratamiento registrado correctamente.")

    except ValueError:
        print("El ID de la consulta debe ser un número.")
    except Exception as e:
        print("Error al insertar el tratamiento:")
        print(e)


def actualizar_tratamiento():
    try:
        tratamiento_dao = TratamientoDAO()

        lista = tratamiento_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay tratamientos registrados.")
            return

        print("\n===== TRATAMIENTOS =====")
        for t in lista:
            print(f"{t.id} - {t.medicamento}")

        id = int(input("\nID del tratamiento a actualizar: "))
        id_consulta = int(input("Nuevo ID de consulta: "))
        medicamento = input("Nuevo medicamento: ")
        dosis = input("Nueva dosis: ")
        fecha_inicio = input("Nueva fecha inicio: ")
        fecha_fin = input("Nueva fecha fin: ")
        indicacion = input("Nuevas indicaciones: ")

        tratamiento = Tratamiento(
            id,
            medicamento,
            dosis,
            fecha_inicio,
            fecha_fin,
            indicacion,
            id_consulta
        )

        tratamiento_dao.actualizar(tratamiento)

        print("\nTratamiento actualizado correctamente.")

    except ValueError:
        print("Datos inválidos.")
    except Exception as e:
        print("Error al actualizar:")
        print(e)


def eliminar_tratamiento():
    try:
        tratamiento_dao = TratamientoDAO()

        lista = tratamiento_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay tratamientos registrados.")
            return

        print("\n===== TRATAMIENTOS =====")
        for t in lista:
            print(f"{t.id} - {t.medicamento}")

        id = int(input("\nID del tratamiento a eliminar: "))

        tratamiento_dao.eliminar(id)

        print("Tratamiento eliminado correctamente.")

    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print("Error al eliminar:")
        print(e)


def menu_tratamientos():
    while True:
        print("\n===== MENÚ TRATAMIENTOS =====")
        print("1. Ver tratamientos")
        print("2. Insertar tratamiento")
        print("3. Actualizar tratamiento")
        print("4. Eliminar tratamiento")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                ver_tratamiento()
            case "2":
                insertar_tratamiento()
            case "3":
                actualizar_tratamiento()
            case "4":
                eliminar_tratamiento()
            case "5":
                break
            case _:
                print("Opción inválida.")





# EMPLEADO

def ver_empleados():
    try:
        empleado_dao = EmpleadoDAO()
        lista = empleado_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay empleados registrados.")
        else:
            print("\n===== LISTA DE EMPLEADOS =====")

            for empleado in lista:
                print(
                    f"ID: {empleado.id}  "
                    f"Nombre: {empleado.nombre}  "
                    f"Apellido Paterno: {empleado.apellido_p} "
                    f"Apellido Materno: {empleado.apellido_m} "
                    f"Usuario/Puesto: {empleado.usuario_puesto}"
                    f"Contraseña: {empleado.contraseña}"
                )

        print("\nConexión exitosa con la base de datos.")

    except Exception as e:
        print("Error al consultar los empleados:")
        print(e)


def insertar_empleado():
    try:
        print("\n===== INSERTAR EMPLEADO =====")

        nombre = input("Nombre: ")
        apellido_p = input("Apellido paterno: ")
        apellido_m = input("Apellido materno: ")
        usuario_puesto = input("Usuario/Puesto: ")
        contraseña = input("Contraseña: ")

        empleado_dao = EmpleadoDAO()

        ultimo_id = empleado_dao.obtener_ultimo_id() + 1

        empleado = Empleado(
            ultimo_id,
            nombre,
            apellido_p,
            apellido_m,
            usuario_puesto,
            contraseña
        )

        empleado_dao.insertar(empleado)

        print("\nEmpleado registrado correctamente.")

    except Exception as e:
        print("Error al insertar el empleado:")
        print(e)


def actualizar_empleado():
    try:
        empleado_dao = EmpleadoDAO()

        lista = empleado_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay empleados registrados.")
            return

        print("\n===== EMPLEADOS =====")

        for empleado in lista:
            print(f"ID: {empleado.id} - {empleado.nombre}")

        id = int(input("\nID del empleado a actualizar: "))
        nombre = input("Nuevo nombre: ")
        apellido_p = input("Nuevo apellido paterno: ")
        apellido_m = input("Nuevo apellido materno: ")
        usuario_puesto = input("Nuevo usuario/puesto: ")
        contraseña = input("Nueva contraseña: ")

        empleado = Empleado(
            id,
            nombre,
            apellido_p,
            apellido_m,
            usuario_puesto,
            contraseña
        )

        empleado_dao.actualizar(empleado)

        print("\nEmpleado actualizado correctamente.")

    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print("Error al actualizar el empleado:")
        print(e)


def eliminar_empleado():
    try:
        empleado_dao = EmpleadoDAO()

        lista = empleado_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay empleados registrados.")
            return

        print("\n===== EMPLEADOS =====")

        for empleado in lista:
            print(f"ID: {empleado.id} - {empleado.nombre}")

        id = int(input("\nID del empleado a eliminar: "))

        empleado_dao.eliminar(id)

        print("\nEmpleado eliminado correctamente.")

    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print("Error al eliminar el empleado:")
        print(e)


def menu_empleados():
    while True:
        print("\n===== MENÚ EMPLEADOS =====")
        print("1. Ver empleados")
        print("2. Insertar empleado")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                ver_empleados()
            case "2":
                insertar_empleado()
            case "3":
                actualizar_empleado()
            case "4":
                eliminar_empleado()
            case "5":
                break
            case _:
                print("Opción inválida.")




# VENTAS



def ver_ventas():
    try:
        ventas_dao = VentasDAO()
        lista = ventas_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay ventas registradas.")
        else:
            print("\n===== LISTA DE VENTAS =====")

            for venta in lista:
                print(
                    f"ID: {venta.id}  "
                    f"Fecha: {venta.fecha_venta}  "
                    f"Producto: {venta.producto_nombre}  "
                    f"Precio: {venta.producto_precio_venta}  "
                    f"Cantidad: {venta.cantidad}  "
                    f"Subtotal: {venta.subtotal}  "
                    f"Total: {venta.total}  "
                    f"ID Producto: {venta.id_producto}"
                )

        print("\nConexión exitosa con la base de datos.")

    except Exception as e:
        print("Error al consultar las ventas:")
        print(e)


def insertar_venta():
    try:
        print("\n===== INSERTAR VENTA =====")

        fecha_venta = input("Fecha de venta (AAAA-MM-DD): ")
        producto_nombre = input("Nombre del producto: ")
        producto_precio_venta = float(input("Precio de venta: "))
        cantidad = int(input("Cantidad: "))

        subtotal = producto_precio_venta * cantidad
        total = subtotal

        id_producto = int(input("ID del producto: "))

        ventas_dao = VentasDAO()

        ultimo_id = ventas_dao.obtener_ultimo_id() + 1

        venta = Ventas(
            ultimo_id,
            fecha_venta,
            producto_nombre,
            producto_precio_venta,
            cantidad,
            subtotal,
            total,
            id_producto
        )

        ventas_dao.insertar(venta)

        print("\nLa venta fue registrada correctamente.")

    except Exception as e:
        print("Error al insertar la venta:")
        print(e)


def actualizar_venta():
    try:
        ventas_dao = VentasDAO()

        lista = ventas_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay ventas registradas.")
            return

        print("\n===== VENTAS =====")

        for venta in lista:
            print(f"ID: {venta.id} - {venta.producto_nombre}")

        id = int(input("\nID de la venta a actualizar: "))
        fecha_venta = input("Nueva fecha: ")
        producto_nombre = input("Nuevo producto: ")
        producto_precio_venta = float(input("Nuevo precio: "))
        cantidad = int(input("Nueva cantidad: "))

        subtotal = producto_precio_venta * cantidad
        total = subtotal

        id_producto = int(input("Nuevo ID del producto: "))

        venta = Ventas(
            id,
            fecha_venta,
            producto_nombre,
            producto_precio_venta,
            cantidad,
            subtotal,
            total,
            id_producto
        )

        ventas_dao.actualizar(venta)

        print("\nLa venta fue actualizada correctamente.")

    except ValueError:
        print("Los datos ingresados son incorrectos.")
    except Exception as e:
        print("Error al actualizar la venta:")
        print(e)


def eliminar_venta():
    try:
        ventas_dao = VentasDAO()

        lista = ventas_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay ventas registradas.")
            return

        print("\n===== VENTAS =====")

        for venta in lista:
            print(f"ID: {venta.id} - {venta.producto_nombre}")

        id = int(input("\nID de la venta a eliminar: "))

        ventas_dao.eliminar(id)

        print("\nLa venta fue eliminada correctamente.")

    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print("Error al eliminar la venta:")
        print(e)


def menu_ventas():
    while True:
        print("\n===== MENÚ VENTAS =====")
        print("1. Ver ventas")
        print("2. Insertar venta")
        print("3. Actualizar venta")
        print("4. Eliminar venta")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                ver_ventas()
            case "2":
                insertar_venta()
            case "3":
                actualizar_venta()
            case "4":
                eliminar_venta()
            case "5":
                break
            case _:
                print("Opción inválida.")
def main():
    menu_principal()


if __name__ == "__main__":
    main()