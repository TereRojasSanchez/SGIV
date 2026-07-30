from database.conexion import Conexion
from models.ventas import Ventas


class VentasDAO:

    
    # OBTENER TODAS LAS VENTAS
    
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT id, fecha_venta, producto_nombre,
               producto_precio_venta, cantidad,
               subtotal, total, id_producto
        FROM "Ventas"
        ORDER BY id
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        ventas = []

        for registro in registros:
            venta = Ventas(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                registro[6],
                registro[7]
            )

            ventas.append(venta)

        cursor.close()
        conexion.close()

        return ventas

    
    # INSERTAR
    
    def insertar(self, venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO "Ventas"
        (
            id,
            fecha_venta,
            producto_nombre,
            producto_precio_venta,
            cantidad,
            subtotal,
            total,
            id_producto
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            venta.id,
            venta.fecha_venta,
            venta.producto_nombre,
            venta.producto_precio_venta,
            venta.cantidad,
            venta.subtotal,
            venta.total,
            venta.id_producto
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    
    # ACTUALIZAR
    
    def actualizar(self, venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE "Ventas"
        SET fecha_venta = %s,
            producto_nombre = %s,
            producto_precio_venta = %s,
            cantidad = %s,
            subtotal = %s,
            total = %s,
            id_producto = %s
        WHERE id = %s
        """

        cursor.execute((
            sql
        ), (
            venta.fecha_venta,
            venta.producto_nombre,
            venta.producto_precio_venta,
            venta.cantidad,
            venta.subtotal,
            venta.total,
            venta.id_producto,
            venta.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    
    # ELIMINAR
    
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        DELETE FROM "Ventas"
        WHERE id = %s
        """

        cursor.execute(sql, (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    
    # OBTENER ÚLTIMO ID
    
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(MAX(id), 0)
        FROM "Ventas"
        """

        cursor.execute(sql)
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]