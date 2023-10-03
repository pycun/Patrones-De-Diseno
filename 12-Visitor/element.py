from abc import ABC, abstractmethod

# Define la interfaz Elemento que declara el método accept
class Elemento(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
