from database.conexion import Conexion
from models.proveedor import Proveedor 

class ProveedorDAO:
    def obtener_todo(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("SELECT * FROM proveedor ")
        registros=cursor.fetchall()

        proveedores=[]
        for registro in registros:
            proveedor =Proveedor(
            id=registro[0],
            nombre=registro[1],
            telefono=registro[2],
            correo=registro[3],
            producto=registro[4]
            )
            proveedores.append(proveedor)
        cursor.close()
        conexion.close()
        return proveedores
    
    def insertar(self,proveedor):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()


        sql="""
        INSERT INTO proveedor (id_proveedor,nombre,telefono,correo,producto)
        VALUES ( %s, %s, %s,%s,%s)
        """
        
            
        cursor.execute(sql,(
            proveedor.id,
            proveedor.nombre,
            proveedor.telefono,
            proveedor.correo,
            proveedor.producto
        
            ))
        
        conexion.commit()
        cursor.close()
        conexion.close()    


    def actualizar(self,proveedor):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        sql="""
        UPDATE proveedor
        SET nombre=%s,telefono=%s, correo=%s, producto=%s
        WHERE id_proveedor=%s
        """

        cursor.execute(sql,(
            proveedor.nombre,
            proveedor.telefono,
            proveedor.correo,
            proveedor.producto,
            proveedor.id
        ))
        conexion.commit()
        cursor.close()
        conexion.close()      

    def obtener_ultimo_id(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("SELECT MAX (id_proveedor) FROM proveedor")
        resultado=cursor.fetchone()

        cursor.close()
        conexion.close()
        
        if resultado[0] is None:
            return 0
        return resultado[0]
    
    def obtener_por_id(self, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        sql = "SELECT id_proveedor, nombre, telefono, correo, producto FROM proveedor WHERE id_proveedor = %s"
        cursor.execute(sql, (id_proveedor,))
        fila = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if fila:
            
            return Proveedor(fila[0], fila[1], fila[2], fila[3], fila[4]) 
        return None
    def eliminar(self,id) :

        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("DELETE FROM proveedor WHERE id_proveedor=%s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()
