from Series import Serie
from Peliculas import Pelicula
from Novelas import Novelas

class Cliente(Serie, Pelicula, Novelas):
    pass
    def __init__(self, buscar, seleccionar):
        self.buscar = buscar
        self.seleccionar = seleccionar

    def ver(self):
        return 'SELECCIONA CATEGORIA DE {} y BUSCA {} PARA VER.'.format(self.buscar, self.seleccionar)


Netflix = Cliente('TERROR...', 'WOLF PACK')
print(Netflix.ver())