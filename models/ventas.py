class Ventas:

    # CONSTRUCTOR

    def __init__(
        self,
        id,
        fecha_venta,
        producto_nombre,
        producto_precio_venta,
        cantidad,
        subtotal,
        total,
        id_producto,
        estado="Pendiente"
    ):

        self.id = id
        self.fecha_venta = fecha_venta
        self.producto_nombre = producto_nombre
        self.producto_precio_venta = producto_precio_venta
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.total = total
        self.id_producto = id_producto
        self.estado = estado

    
    # CONFIRMAR VENTA
    
    def confirmar_venta(self):
        self.estado = "Confirmada"
    
    # CANCELAR VENTA
    
    def cancelar_venta(self):
        self.estado = "Cancelada"
 
    # CALCULAR SUBTOTAL Y TOTAL

    def calcular_total(self):
        self.subtotal = self.producto_precio_venta * self.cantidad
        self.total = self.subtotal

    
    def mostrar_info(self):

        print(f"ID: {self.id}")
        print(f"Fecha: {self.fecha_venta}")
        print(f"Producto: {self.producto_nombre}")
        print(f"Precio: ${self.producto_precio_venta:.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Total: ${self.total:.2f}")
        print(f"ID Producto: {self.id_producto}")
        print(f"Estado: {self.estado}")