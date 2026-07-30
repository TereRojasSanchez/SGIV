from database.conexion import Conexion
from models.tratamiento import Tratamiento


class TratamientoDAO:

    # ==========================
    # OBTENER TODOS
    # ==========================
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT id, medicamento, dosis, fecha_inicio,
               fecha_fin, indicacion, id_consulta
        FROM "Tratamiento"
        ORDER BY id;
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        tratamientos = []

        for registro in registros:
            tratamiento = Tratamiento(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                registro[6]
            )
            tratamientos.append(tratamiento)

        cursor.close()
        conexion.close()

        return tratamientos

    # ==========================
    # INSERTAR
    # ==========================
    def insertar(self, tratamiento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO "Tratamiento"
        (medicamento, dosis, fecha_inicio, fecha_fin, indicacion, id_consulta)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            tratamiento.medicamento,
            tratamiento.dosis,
            tratamiento.fecha_inicio,
            tratamiento.fecha_fin,
            tratamiento.indicacion,
            tratamiento.id_consulta
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ==========================
    # ACTUALIZAR
    # ==========================
    def actualizar(self, tratamiento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE "Tratamiento"
        SET medicamento = %s,
            dosis = %s,
            fecha_inicio = %s,
            fecha_fin = %s,
            indicacion = %s,
            id_consulta = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            tratamiento.medicamento,
            tratamiento.dosis,
            tratamiento.fecha_inicio,
            tratamiento.fecha_fin,
            tratamiento.indicacion,
            tratamiento.id_consulta,
            tratamiento.id
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
        DELETE FROM "Tratamiento"
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
        FROM "Tratamiento"
        """

        cursor.execute(sql)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]