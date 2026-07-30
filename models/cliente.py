class Cliente:
    # Constructor
    def __init__(self, id, nombre, apellido_paterno, apellido_materno, telefono, correo, calle, no_exterior, no_interior, colonia, municipio, codigo_postal, activo=True):
        self.id = id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.correo = correo
        self.calle = calle
        self.no_exterior = no_exterior
        self.no_interior = no_interior  
        self.colonia = colonia
        self.municipio = municipio
        self.codigo_postal = codigo_postal
        self.activo = activo 

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Apellido Paterno: {self.apellido_paterno}, "
                f"Apellido Materno: {self.apellido_materno}, Teléfono: {self.telefono}, Correo: {self.correo}, "
                f"Calle: {self.calle}, No. Exterior: {self.no_exterior}, No. Interior: {self.no_interior}, "
                f"Colonia: {self.colonia}, Municipio: {self.municipio}, CP: {self.codigo_postal}, Activo: {self.activo}")