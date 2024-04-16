from Evento import evento

class TrabajoPractico (evento):
    def __init__(self,fecha,temas,materia):
        super().__init__(self,fecha)
        self.materia=materia
        self.temas=temas

    def __str__(self):
        return f"Fecha de Trabajo Practico: {self.fecha}, Materia: {self.materia} , Temas {self.temas} "
        