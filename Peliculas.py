class Pelicula:
    def __init__(self,nombre):
        self.nombre = nombre

    def accion(self):
        return'LA PELICULA DE ACCIÓN ES: {}'.format(self.nombre)
    
Carreras = Pelicula('RÁPIDOS Y FURIOSOS')
print(Carreras.accion())