from database.conexion import Conexion
from models.producto import Producto


class ProductoDAO:
    def obtener_todo(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("SELECT * FROM producto ")
        registros=cursor.fetchall()

        productos=[]
        for registro in registros:
            producto =Producto(
            id=registro[0],
            nombre=registro[1],
            precio_compra=registro[2],
            precio_venta=registro[3],
            tipo=registro[4],
            lote=registro[5],
            stock_maximo=[6],
            stock_minimo=[7],
            existencia=True,
            fecha_caducidad=[8]
            )
            productos.append(producto)
        cursor.close()
        conexion.close()
        return productos
    
    def insertar(self,producto):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()


        sql="""
        INSERT INTO producto (id,nombre,precio_compra,precio_venta,tipo,lote,stock_maximo,stock_minimo,existencia,fecha_caducidad)
        VALUES ( %s, %s, %s,%s ,%s ,%s ,%s ,%s ,%s ,%s )
        """
        
            
        cursor.execute(sql,(
            producto.id,
            producto.nombre,
            producto.precio_compra,
            producto.precio_venta,
            producto.tipo,
            producto.lote,
            producto.stock_maximo,
            producto.stock_minimo,
            producto.existencia,
            producto.fecha_caducidad
        
            ))
        
        conexion.commit()
        cursor.close()
        conexion.close()   

    def actualizar(self,producto):
         conexion=Conexion.obtener_conexion()
         cursor=conexion.cursor()
         
         sql="""
            UPDATE producto
             SET nombre=%s,precio_compra=%s,precio_venta=%s,tipo=%s,lote=%s,stock_maximo=%s,stock_minimo=%s,existencia=%s,fecha_caducidad=%s
             WHERE id=%s
             """
         
         cursor.execute(sql,(
                producto.nombre,
                producto.precio_compra,
                producto.precio_venta,
                producto.tipo,
                producto.lote,
                producto.stock_maximo,
                producto.stock_minimo,
                producto.existencia,
                producto.fecha_caducidad,
                producto.id
                 ))
         conexion.commit()
         cursor.close()
         conexion.close()      
         
    def obtener_ultimo_id(self):
                 conexion=Conexion.obtener_conexion()
                 cursor=conexion.cursor()
         
                 cursor.execute("SELECT MAX (id) FROM producto")
                 resultado=cursor.fetchone()
         
                 cursor.close()
                 conexion.close()
                 
                 if resultado[0] is None:
                     return 0
                 return resultado[0]
             
    def obtener_por_id(self, id):
                 conexion = Conexion.obtener_conexion()
                 cursor = conexion.cursor()
                 
                 sql = "SELECT id, nombre,precio_compra,precio_venta,tipo,lote,stock_maximo,stock_minimo,existencia,fecha_caducidad FROM producto WHERE id = %s"
                 cursor.execute(sql, (id,))
                 fila = cursor.fetchone()
                 
                 cursor.close()
                 conexion.close()
                 
                 if fila:
                     
                  return Producto(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5],fila[6],fila[7],fila[8],fila[9]) 
                 return None
    def eliminar(self,id) :
         
                 conexion=Conexion.obtener_conexion()
                 cursor=conexion.cursor()
         
                 cursor.execute("DELETE FROM producto  WHERE id=%s",(id,))
         
                 conexion.commit()
                 cursor.close()
                 conexion.close()