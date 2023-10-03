from element import Elemento


# Define las clases de los edificios que pueden ser visitados y las hace elementos visitables
class Edificio(Elemento):
    pass


class EdificioResidencial(Edificio):
    def __init__(self) -> None:
        self._precio = 100
    def accept(self, visitor):
        visitor.visit_edificio_residencial(self)


class Banco(Edificio):
    def __init__(self) -> None:
        self._precio = 200
    def accept(self, visitor):
        visitor.visit_banco(self)


class Cafeteria(Edificio):
    def __init__(self) -> None:
        self._precio = 300
    def accept(self, visitor):
        visitor.visit_cafeteria(self)

