class Serie:
    def __init__(self,nombre):
        self.nombre = nombre

    def terror(self):
        return'LA SERIE DE LOBOS SE LLAMA: {}'.format(self.nombre)
    
Supervivencia = Serie('WOLF PACK')
print(Supervivencia.terror())