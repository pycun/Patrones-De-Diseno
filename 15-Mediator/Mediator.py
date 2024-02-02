from __future__ import annotations
from abc import ABC


class Mediador(ABC):
    """
    La interfaz de Mediador declara un método utilizado por los componentes para notificar al
    mediador sobre varios eventos. El mediador puede reaccionar a estos eventos y
    pasar la ejecución a otros componentes.
    """

    def notificar(self, remitente: object, evento: str) -> None:
        pass


class MediadorConcreto(Mediador):
    def __init__(self, componente1: Componente1, componente2: Componente2) -> None:
        """
        Inicializa el Mediador Concreto con referencias a los Componentes.
        """
        self._componente1 = componente1
        self._componente1.mediador = self
        self._componente2 = componente2
        self._componente2.mediador = self

    def notificar(self, remitente: object, evento: str) -> None:
        """
        Implementa el método notificar de la interfaz del Mediador. Reacciona a eventos
        específicos y desencadena operaciones en los componentes correspondientes.
        """
        if evento == "A":
            print("El mediador reacciona a A y desencadena las siguientes operaciones:")
            self._componente2.hacer_c()
        elif evento == "D":
            print("El mediador reacciona a D y desencadena las siguientes operaciones:")
            self._componente1.hacer_b()
            self._componente2.hacer_c()


class ComponenteBase:
    """
    El Componente Base proporciona la funcionalidad básica de almacenar una instancia del mediador
    dentro de los objetos de componente.
    """

    def __init__(self, mediador: Mediador = None) -> None:
        """
        Inicializa el Componente Base con una referencia al Mediador.
        """
        self._mediador = mediador

    @property
    def mediador(self) -> Mediador:
        return self._mediador

    @mediador.setter
    def mediador(self, mediador: Mediador) -> None:
        """
        Permite establecer el Mediador después de la creación del componente.
        """
        self._mediador = mediador


"""
Los Componentes Concretos implementan varias funcionalidades. No dependen de otros
componentes. Tampoco dependen de ninguna clase concreta de mediador.
"""


class Componente1(ComponenteBase):
    def hacer_a(self) -> None:
        """
        Realiza la operación A y notifica al Mediador.
        """
        print("Componente 1 hace A.")
        self.mediador.notificar(self, "A")

    def hacer_b(self) -> None:
        """
        Realiza la operación B y notifica al Mediador.
        """
        print("Componente 1 hace B.")
        self.mediador.notificar(self, "B")


class Componente2(ComponenteBase):
    def hacer_c(self) -> None:
        """
        Realiza la operación C y notifica al Mediador.
        """
        print("Componente 2 hace C.")
        self.mediador.notificar(self, "C")

    def hacer_d(self) -> None:
        """
        Realiza la operación D y notifica al Mediador.
        """
        print("Componente 2 hace D.")
        self.mediador.notificar(self, "D")


if __name__ == "__main__":
    # Código del cliente.
    c1 = Componente1()
    c2 = Componente2()
    mediador = MediadorConcreto(c1, c2)

    print("El cliente desencadena la operación A.")
    c1.hacer_a()

    print("\n", end="")

    print("El cliente desencadena la operación D.")
    c2.hacer_d()
