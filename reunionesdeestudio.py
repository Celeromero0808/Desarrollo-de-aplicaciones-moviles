from Evento import evento

class ReunionEstudio (evento) :
    def __init__(self,fecha,descripcion,ubicacion):
        super().__init__(self,fecha,descripcion)
        self.ubicacion=ubicacion

    def __str__(self):
        return f"Fecha de la reunion: {self.fecha}, Descripción: {self.descripcion} , ubicacion {self.ubicacion} "
        