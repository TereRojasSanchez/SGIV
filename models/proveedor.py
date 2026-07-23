class Proveedor:
#constructor
    def __init__(self,id,nombre,telefono,correo,producto):
        self.id=id
        self.nombre = nombre
        self.telefono=telefono
        self.correo=correo
        self.producto=producto

    def mostrar_info(self):
        return f"ID: {self.id}, NOMBRE: {self.nombre} , TELEFONO: {self.telefono}, CORREO:{self.correo}, PRODUCTO:{self.producto}"