from database.conexion import Conexion
from models.empleado import Empleado


class EmpleadoDAO:

    # ==========================
    # OBTENER TODOS
    # ==========================
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT id, nombre, apellido_p, apellido_m,
               usuario_puesto, contraseña
        FROM "Empleado"
        ORDER BY id
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        empleados = []

        for registro in registros:
            empleado = Empleado(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5]
            )

            empleados.append(empleado)

        cursor.close()
        conexion.close()

        return empleados

    # ==========================
    # INSERTAR
    # ==========================
    def insertar(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO "Empleado"
        (
            id,
            nombre,
            apellido_p,
            apellido_m,
            usuario_puesto,
            contraseña
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            empleado.id,
            empleado.nombre,
            empleado.apellido_p,
            empleado.apellido_m,
            empleado.usuario_puesto,
            empleado.contraseña
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ==========================
    # ACTUALIZAR
    # ==========================
    def actualizar(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE "Empleado"
        SET
            nombre = %s,
            apellido_p = %s,
            apellido_m = %s,
            usuario_puesto = %s,
            contraseña = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            empleado.nombre,
            empleado.apellido_p,
            empleado.apellido_m,
            empleado.usuario_puesto,
            empleado.contraseña,
            empleado.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ==========================
    # ELIMINAR
    # ==========================
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        DELETE FROM "Empleado"
        WHERE id = %s
        """

        cursor.execute(sql, (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ==========================
    # OBTENER ÚLTIMO ID
    # ==========================
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(MAX(id), 0)
        FROM "Empleado"
        """

        cursor.execute(sql)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]