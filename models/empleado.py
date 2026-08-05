class Empleado:
    def __init__(self, id, usuario, password, nombre, apellidop, apellidom,
                 correo=None, telefono=None, activo=True,
                 fecha_alta=None, fecha_baja=None, curp=None,
                 rfc=None, horario=None, turno=None, rol=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.correo = correo
        self.telefono = telefono
        self.activo = activo
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.curp = curp
        self.rfc = rfc
        self.horario = horario
        self.turno = turno
        self.rol = rol

    # Método auxiliar para obtener nombre completo
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidop} {self.apellidom}"

    # Convertir objeto a diccionario (útil para devolver datos al DAO/UI)
    def to_dict(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "nombre_completo": self.nombre_completo(),
            "rol": self.rol,
            "activo": self.activo
        }