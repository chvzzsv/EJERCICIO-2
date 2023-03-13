class Novelas:
    def __init__(self,nombre):
        self.nombre = nombre

    def comedia(self):
        return'LA NOVELA DE COMEDIA ES: {}'.format(self.nombre)
    
Familiar = Novelas('AL FONDO HAY SITIO')
print(Familiar.comedia())