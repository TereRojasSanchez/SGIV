from database.conexion import Conexion
from models.empleado import Empleado


class EmpleadoDAO:

    def obtener_todo(self):

        conexion = None
        cursor = None

        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
                SELECT
                    id,
                    nombre,
                    apellido_paterno,
                    apellido_materno,
                    telefono,
                    correo,
                    usuario,
                    contraseña,
                    municipio,
                    codigo_postal,
                    colonia,
                    calle,
                    numero_exterior,
                    numero_interior,
                    activo,
                    puesto_usuario
                FROM "Empleado"
                ORDER BY id;
            """

            cursor.execute(sql)

            empleados = []

            for fila in cursor.fetchall():

                empleado = Empleado(
                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6],
                    fila[7],
                    fila[8],
                    fila[9],
                    fila[10],
                    fila[11],
                    fila[12],
                    fila[13],
                    fila[14],
                    fila[15]
                )

                empleados.append(empleado)

            return empleados

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()


    
    # OBTENER EMPLEADO POR ID
    def obtener_por_id(self, empleado_id):

        conexion = None
        cursor = None

        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
                SELECT
                    id,
                    nombre,
                    apellido_paterno,
                    apellido_materno,
                    telefono,
                    correo,
                    usuario,
                    contraseña,
                    municipio,
                    codigo_postal,
                    colonia,
                    calle,
                    numero_exterior,
                    numero_interior,
                    activo,
                    puesto_usuario
                FROM "Empleado"
                WHERE id = %s;
            """

            cursor.execute(
                sql,
                (empleado_id,)
            )

            fila = cursor.fetchone()

            if fila:

                return Empleado(
                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6],
                    fila[7],
                    fila[8],
                    fila[9],
                    fila[10],
                    fila[11],
                    fila[12],
                    fila[13],
                    fila[14],
                    fila[15]
                )

            return None

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    # INSERTAR EMPLEADO
    def insertar(self, empleado):

        conexion = None
        cursor = None

        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
                INSERT INTO "Empleado"
                (
                    nombre,
                    apellido_paterno,
                    apellido_materno,
                    telefono,
                    correo,
                    usuario,
                    contraseña,
                    municipio,
                    codigo_postal,
                    colonia,
                    calle,
                    numero_exterior,
                    numero_interior,
                    activo,
                    puesto_usuario
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                );
            """

            valores = (
                empleado.nombre,
                empleado.apellido_paterno,
                empleado.apellido_materno,
                empleado.telefono,
                empleado.correo,
                empleado.usuario,
                empleado.contraseña,
                empleado.municipio,
                empleado.codigo_postal,
                empleado.colonia,
                empleado.calle,
                empleado.numero_exterior,
                empleado.numero_interior,
                empleado.activo,
                empleado.puesto_usuario
            )

            cursor.execute(
                sql,
                valores
            )

            conexion.commit()

        except Exception as error:

            if conexion:
                conexion.rollback()

            raise error

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()
    # ACTUALIZAR EMPLEADO

    def actualizar(self, empleado):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
                UPDATE "Empleado"
                SET
                    nombre = %s,
                    apellido_paterno = %s,
                    apellido_materno = %s,
                    telefono = %s,
                    correo = %s,
                    usuario = %s,
                    contraseña = %s,
                    municipio = %s,
                    codigo_postal = %s,
                    colonia = %s,
                    calle = %s,
                    numero_exterior = %s,
                    numero_interior = %s,
                    activo = %s,
                    puesto_usuario = %s
                WHERE id = %s;
            """

            valores = (
                empleado.nombre,
                empleado.apellido_paterno,
                empleado.apellido_materno,
                empleado.telefono,
                empleado.correo,
                empleado.usuario,
                empleado.contraseña,
                empleado.municipio,
                empleado.codigo_postal,
                empleado.colonia,
                empleado.calle,
                empleado.numero_exterior,
                empleado.numero_interior,
                empleado.activo,
                empleado.puesto_usuario,
                empleado.id
            )

            cursor.execute(
                sql,
                valores
            )

            if cursor.rowcount == 0:

                raise Exception(
                    "No se encontró el empleado que deseas actualizar."
                )

            conexion.commit()

        except Exception as error:

            if conexion:
                conexion.rollback()

            raise error

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()


    def eliminar(self, empleado_id):

        conexion = None
        cursor = None

        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """
                UPDATE "Empleado"
                SET activo = FALSE
                WHERE id = %s;
            """

            cursor.execute(
                sql,
                (empleado_id,)
            )

            if cursor.rowcount == 0:

                conexion.rollback()

                raise Exception(
                    "No se encontró el empleado con ese ID."
                )

            conexion.commit()

            return True

        except Exception as error:

            if conexion:
                conexion.rollback()

            raise Exception(
                f"No se pudo eliminar el empleado: {error}"
            )

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    # ACTIVAR EMPLEADO

    def activar(self, empleado_id):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            sql = """
                UPDATE "Empleado"
                SET activo = TRUE
                WHERE id = %s;
            """

            cursor.execute(
                sql,
                (empleado_id,)
            )

            if cursor.rowcount == 0:

                conexion.rollback()

                raise Exception(
                    "No se encontró el empleado con ese ID."
                )

            conexion.commit()
            return True

        except Exception as error:

            if conexion:
                conexion.rollback()
            raise error

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()