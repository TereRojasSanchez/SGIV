class Empleado:

    
    def __init__(self, id, nombre, apellido_p, apellido_m, usuario_puesto, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.usuario_puesto = usuario_puesto
        self.contraseña = contraseña

    
    def activar(self):
        self.activo = True

    
    def desactivar(self):
        self.activo = False

    
    def mostrar_info(self):
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido Paterno: {self.apellido_p}\n"
            f"Apellido Materno: {self.apellido_m}\n"
            f"Usuario/Puesto: {self.usuario_puesto}\n"
            f"Contraseña: {self.contraseña}"
        )