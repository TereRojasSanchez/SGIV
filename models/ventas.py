class Ventas:

    # Constructor
    def __init__(self, id, fecha_venta, producto_nombre,
                 producto_precio_venta, cantidad,
                 subtotal, total, id_producto,
                 estado="Pendiente"):
 
        self.id = id
        self.fecha_venta = fecha_venta
        self.producto_nombre = producto_nombre
        self.producto_precio_venta = producto_precio_venta
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.total = total
        self.id_producto = id_producto
        self.estado = estado

    # Confirmar venta
    def confirmar_venta(self):
        self.estado = "Confirmada"

    # Cancelar venta
    def cancelar_venta(self):
        self.estado = "Cancelada"

    # Mostrar información
    def mostrar_info(self):
        return (
            f"ID Venta: {self.id}\n"
            f"Fecha de venta: {self.fecha_venta}\n"
            f"Producto: {self.producto_nombre}\n"
            f"Precio de venta: ${self.producto_precio_venta:.2f}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Subtotal: ${self.subtotal:.2f}\n"
            f"Total: ${self.total:.2f}\n"
            f"ID Producto: {self.id_producto}\n"
            f"Estado: {self.estado}"
        )