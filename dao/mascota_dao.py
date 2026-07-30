from database.conexion import Conexion
from models.mascota import Mascota


class MascotaDAO:

    
    # OBTENER ID DE LA ESPECIE

    def _obtener_id_especie(self, cursor, especie):

        if str(especie).isdigit():
            return int(especie)

        sql = """
            SELECT id_especie
            FROM public."Especie"
            WHERE LOWER(nombre_especie)=LOWER(%s)
        """

        cursor.execute(sql, (especie,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        raise Exception(f"La especie '{especie}' no existe.")

    
    # OBTENER TODAS LAS ESPECIES
    
    def obtener_especies(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT id_especie, nombre_especie
        FROM public."Especie"
        ORDER BY id_especie;
        """

        cursor.execute(sql)

        especies = cursor.fetchall()

        cursor.close()
        conexion.close()

        return especies

    
    # VER TODAS LAS MASCOTAS
    
    def obtener_todo(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id,
            id_cliente,
            nombre,
            raza,
            id_especie,
            edad,
            peso
        FROM mascota
        ORDER BY id;
        """

        cursor.execute(sql)

        registros = cursor.fetchall()

        mascotas = []

        for registro in registros:

            mascota = Mascota(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                registro[6]
            )

            mascotas.append(mascota)

        cursor.close()
        conexion.close()

        return mascotas

    
    # INSERTAR MASCOTA
    
    def insertar(self, mascota):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            id_especie = self._obtener_id_especie(cursor, mascota.especie)

            sql = """
            INSERT INTO mascota
            (id_cliente, nombre, raza, id_especie, edad, peso)
            VALUES (%s,%s,%s,%s,%s,%s)
            """

            cursor.execute(sql, (
                mascota.id_cliente,
                mascota.nombre,
                mascota.raza,
                id_especie,
                mascota.edad,
                mascota.peso
            ))

            conexion.commit()

        except Exception as e:
            conexion.rollback()
            raise Exception(e)

        finally:
            cursor.close()
            conexion.close()

    
    # ACTUALIZAR MASCOTA
    
    def actualizar(self, mascota):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            id_especie = self._obtener_id_especie(cursor, mascota.especie)

            sql = """
            UPDATE mascota
            SET
                id_cliente=%s,
                nombre=%s,
                raza=%s,
                id_especie=%s,
                edad=%s,
                peso=%s
            WHERE id=%s
            """

            cursor.execute(sql, (
                mascota.id_cliente,
                mascota.nombre,
                mascota.raza,
                id_especie,
                mascota.edad,
                mascota.peso,
                mascota.id
            ))

            conexion.commit()

        except Exception as e:
            conexion.rollback()
            raise Exception(e)

        finally:
            cursor.close()
            conexion.close()

    
    # ELIMINAR MASCOTA
    
    def eliminar(self, id):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            sql = "DELETE FROM mascota WHERE id=%s"

            cursor.execute(sql, (id,))

            conexion.commit()

        except Exception as e:
            conexion.rollback()
            raise Exception(e)

        finally:
            cursor.close()
            conexion.close()

    
    # OBTENER ÚLTIMO ID
    
    def obtener_ultimo_id(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            cursor.execute("SELECT COALESCE(MAX(id),0) FROM mascota")

            ultimo = cursor.fetchone()[0]

            return ultimo

        finally:
            cursor.close()
            conexion.close()