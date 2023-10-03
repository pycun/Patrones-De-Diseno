from abc import ABC, abstractmethod
from concrete_element import EdificioResidencial, Banco, Cafeteria

# Define la interfaz Visitor que declara los métodos visit para cada tipo de edificio
class Visitante(ABC):
    @abstractmethod
    def visit_edificio_residencial(self, edificio_residencial: EdificioResidencial) -> None:
        pass

    @abstractmethod
    def visit_banco(self, banco: Banco) -> None:
        pass

    @abstractmethod
    def visit_cafeteria(self, cafeteria: Cafeteria) -> None:
        pass