class Mascota:
    # Constructor
    def __init__(self, id, id_cliente, nombre, raza, especie, edad, peso):
        self.id = id
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.activo = True

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return (
            f"ID: {self.id}, "
            f"ID Cliente: {self.id_cliente}, "
            f"Nombre: {self.nombre}, "
            f"Raza: {self.raza}, "
            f"Especie: {self.especie}, "
            f"Edad: {self.edad}, "
            f"Peso: {self.peso}"
        )



