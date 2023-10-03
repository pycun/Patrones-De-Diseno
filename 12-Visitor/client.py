from typing import List
from concrete_visitor import AgenteDeSeguros, AgenteDeVentas
from visitor import Visitante
from concrete_element import Edificio , EdificioResidencial, Banco, Cafeteria

# Puedes realizar múltiples operaciones diferentes en los elementos sin modificar sus clases.
def cliente_edificios(edificios: List[Edificio], visitante: Visitante) -> None:
    for edificio in edificios:
        edificio.accept(visitante)

if __name__ == "__main__":
    #Obtenemos las intancias(Objetos antiguos) de los edificios
    edificios = [EdificioResidencial(), Banco(), Cafeteria()]
    print("\n")
    print("El agente de seguros visita los edificios y ofrece seguros específicos:")
    agente_seguros = AgenteDeSeguros()
    agente_ventas = AgenteDeVentas()
    cliente_edificios(edificios, agente_seguros)
    print("\n------------------------------------------------------------------\n")
    print("El agente de ventas visita los edificios y ofrece productos específicos:")
    cliente_edificios(edificios, agente_ventas)
    print("\n")