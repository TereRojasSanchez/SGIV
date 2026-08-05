from database.conexion import Conexion
from models.empleado import Empleado

def validar_usuario(usuario, password):
    conexion = Conexion.obtener_conexion()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conexion.cursor()
        query = """
            SELECT id, usuario, password, nombre, apellidop, apellidom, rol, activo
            FROM empleado
            WHERE usuario = %s 
              AND password = %s 
              AND activo = TRUE
        """
        cursor.execute(query, (usuario, password))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return Empleado(
                id=resultado[0],
                usuario=resultado[1],
                password=resultado[2],
                nombre=resultado[3],
                apellidop=resultado[4],
                apellidom=resultado[5],
                rol=resultado[6],
                activo=resultado[7]
            )
        return None

    except Exception as e:
        print("Error al validar el usuario:", e)
        if conexion:
            conexion.close()
        return None