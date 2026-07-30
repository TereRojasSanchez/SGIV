import psycopg2
from database.conexion import Conexion
from models.cliente import Cliente

class ClienteDAO:

    # OBTENER TODOS
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM cliente")
        registros = cursor.fetchall()

        clientes = []

        for registro in registros:
            cliente = Cliente(
                id=registro[0],
                nombre=registro[1],
                apellido_paterno=registro[2],
                apellido_materno=registro[3],
                telefono=registro[4],
                correo=registro[5],
                calle=registro[6],
                no_exterior=registro[7],
                no_interior=registro[8],
                colonia=registro[9],
                municipio=registro[10],
                codigo_postal=registro[11]
            )

            clientes.append(cliente)

        cursor.close()
        conexion.close()

        return clientes

    # INSERTAR
    def insertar(self, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
            INSERT INTO cliente
            (nombre, apellido_paterno, apellido_materno, telefono, correo,
            calle, no_exterior, no_interior, colonia, municipio, codigo_postal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(sql, (
                cliente.nombre,
                cliente.apellido_paterno,
                cliente.apellido_materno,
                cliente.telefono,
                cliente.correo,
                cliente.calle,
                cliente.no_exterior,
                cliente.no_interior,
                cliente.colonia,
                cliente.municipio,
                cliente.codigo_postal
            ))

            conexion.commit()
            cursor.close()

        except Exception as e:
            print(f"\n[Error de Postgres] -> {e}")
            raise e

        finally:
            if conexion is not None:
                conexion.close()

    # ACTUALIZAR
    def actualizar(self, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
            UPDATE cliente
            SET
                nombre = %s,
                apellido_paterno = %s,
                apellido_materno = %s,
                telefono = %s,
                correo = %s,
                calle = %s,
                no_exterior = %s,
                no_interior = %s,
                colonia = %s,
                municipio = %s,
                codigo_postal = %s
            WHERE id = %s
            """

            cursor.execute(sql, (
                cliente.nombre,
                cliente.apellido_paterno,
                cliente.apellido_materno,
                cliente.telefono,
                cliente.correo,
                cliente.calle,
                cliente.no_exterior,
                cliente.no_interior,
                cliente.colonia,
                cliente.municipio,
                cliente.codigo_postal,
                cliente.id
            ))

            conexion.commit()
            cursor.close()

        except Exception as e:
            print(f"\n[Error de Postgres] -> {e}")
            raise e

        finally:
            if conexion is not None:
                conexion.close()

    # ELIMINAR
    def eliminar(self, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))

            conexion.commit()
            cursor.close()

        except Exception as e:
            print(f"\n[Error de Postgres] -> {e}")
            raise e

        finally:
            if conexion is not None:
                conexion.close()

    # OBTENER ÚLTIMO ID
    def obtener_ultimo_id(self):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("SELECT MAX(id) FROM cliente")
            resultado = cursor.fetchone()

            cursor.close()

            if resultado is None or resultado[0] is None:
                return 0

            return resultado[0]

        except Exception as e:
            print(f"Error en BD al obtener último ID: {e}")
            return 0

        finally:
            if conexion is not None:
                conexion.close()