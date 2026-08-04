class Mascota:

    def __init__(self, id, id_cliente, nombre, raza, id_especie, edad, peso):
        self.id = id
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.raza = raza
        self.id_especie = id_especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return (
            f"ID: {self.id}, "
            f"ID Cliente: {self.id_cliente}, "
            f"Nombre: {self.nombre}, "
            f"Raza: {self.raza}, "
            f"ID Especie: {self.id_especie}, "
            f"Edad: {self.edad}, "
            f"Peso: {self.peso}"
        )