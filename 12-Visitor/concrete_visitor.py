from visitor import Visitante
from concrete_element import EdificioResidencial, Banco, Cafeteria

#Se obtiene los metodos de la IVisitor y aqui se puede crear las operaciones para poder ser utlizadas


class AgenteDeSeguros(Visitante):
    def visit_edificio_residencial(self, edificio_residencial: EdificioResidencial) -> None:
        print(F"Ofreciendo seguros médicos a un {edificio_residencial.__class__.__name__} y tiene un precio de {edificio_residencial._precio}")

    def visit_banco(self, banco: Banco) -> None:
        print(F"Ofreciendo seguros contra robos a un {banco.__class__.__name__} y tiene un precio de {banco._precio}")

    def visit_cafeteria(self, cafeteria: Cafeteria) -> None:        print(F"Ofreciendo seguros contra incendios e inundaciones a una {cafeteria.__class__.__name__} y tiene un precio de {cafeteria._precio}")


class AgenteDeVentas(Visitante):
    def visit_edificio_residencial(self, edificio_residencial: EdificioResidencial) -> None:
        print(F"Ofreciendo productos a un {edificio_residencial.__class__.__name__}")

    def visit_banco(self, banco: Banco) -> None:
        print(F"Ofreciendo productos a un {banco.__class__.__name__}")

    def visit_cafeteria(self, cafeteria: Cafeteria) -> None:
        print(F"Ofreciendo productos a una {cafeteria.__class__.__name__}")