class Tratamiento:

    # Constructor 
    def __init__(self, id, medicamento, dosis, fecha_inicio, fecha_fin, indicacion, id_consulta):
        self.id = id 
        self.medicamento = medicamento
        self.dosis = dosis
        self.fecha_inicio = fecha_inicio
        self.fecha_fin= fecha_fin
        self.indicacion = indicacion
        self.id_consulta = id_consulta

        def activar(self):
                self.activo = True
        
        def desactivar(self):
                self.activo = False
        

        def mostrar_info(self):
                return (
                    f"ID: {self.id}, "
                    f"Medicamento: {self.medicamento}, "
                    f"Dosis: {self.dosis}, "
                    f"Fecha_inicio: {self.fecha_inicio}, "
                    f"Fecha_fin: {self.fecha_fin}, "
                    f"Indicacion: {self.indicacion}, "
                    f"id_consulta: {self.id_consulta}"
                )