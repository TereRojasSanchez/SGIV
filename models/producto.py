class Producto:
    #constructor
    def __init__(self, id,nombre,precio_compra,precio_venta,tipo,lote,stock_maximo,stock_minimo,existencia):
        self.id = id 
        self.nombre=nombre
        self.precio_compra=precio_compra
        self.precio_venta=precio_venta
        self.tipo=tipo
        self.lote=lote
        self.stock_maximo=stock_maximo
        self.stockminimo=stock_minimo
        self.existencia=existencia

    def devolver(self):
        self.existencia = False    

    def devolver(self):
        self.existencia = True   


    def mostrar_info(self):
        self.existencia = "Disponible" if self.existencia else "No disponible"
        return f"ID:{self.id}, Nombre:{self.nombre}, Precio de proveedor: {self.precio_compra}, Precio venta:{self.precio_venta},Tipo:{self.tipo},Lote:{self.lote}, stock maximo:{self.stock_maximo},stock minimo: {self.stockminimo}"