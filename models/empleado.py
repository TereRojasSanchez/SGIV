class Empleado:

    def __init__(
        self,
        id,
        nombre,
        apellido_paterno,
        apellido_materno,
        telefono,
        correo,
        usuario,
        contraseña,
        municipio,
        codigo_postal,
        colonia,
        calle,
        numero_exterior,
        numero_interior,
        activo,
        puesto_usuario
    ):

        self.id = id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.correo = correo
        self.usuario = usuario
        self.contraseña = contraseña
        self.municipio = municipio
        self.codigo_postal = codigo_postal
        self.colonia = colonia
        self.calle = calle
        self.numero_exterior = numero_exterior
        self.numero_interior = numero_interior
        self.activo = activo
        self.puesto_usuario = puesto_usuario


    # ==========================
    # ACTIVAR EMPLEADO
    # ==========================

    def activar(self):
        self.activo = True


    # ==========================
    # DESACTIVAR EMPLEADO
    # ==========================

    def desactivar(self):
        self.activo = False


    # ==========================
    # MOSTRAR INFORMACIÓN
    # ==========================

    def mostrar_info(self):

        return (

            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido Paterno: {self.apellido_paterno}\n"
            f"Apellido Materno: {self.apellido_materno}\n"
            f"Teléfono: {self.telefono}\n"
            f"Correo: {self.correo}\n"
            f"Usuario: {self.usuario}\n"
            f"Contraseña: {self.contraseña}\n"
            f"Municipio: {self.municipio}\n"
            f"Código Postal: {self.codigo_postal}\n"
            f"Colonia: {self.colonia}\n"
            f"Calle: {self.calle}\n"
            f"Número Exterior: {self.numero_exterior}\n"
            f"Número Interior: {self.numero_interior}\n"
            f"Activo: {self.activo}\n"
            f"Puesto: {self.puesto_usuario}"

        )