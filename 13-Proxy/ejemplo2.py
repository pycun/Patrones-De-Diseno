from abc import ABC, abstractmethod

# Clase abstracta que define la interfaz de la imagen
class Imagen(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Implementación concreta de la imagen
class ImagenReal(Imagen):
    def __init__(self, nombre):
        self.nombre = nombre
        self.cargada = False

    def cargar(self):
        if not self.cargada:
            print(f"Cargando imagen: {self.nombre}")
            self.cargada = True

    def mostrar(self):
        self.cargar()
        print(f"Mostrando imagen: {self.nombre}")

# Proxy que controla el acceso a la imagen
class ProxyImagen(Imagen):
    def __init__(self, imagen_real):
        self.imagen_real = imagen_real

    def mostrar(self):
        print("Acceso controlado por el Proxy.")
        self.imagen_real.mostrar()

# Ejemplo de uso
if __name__ == '__main__':
    imagen_real = ImagenReal("foto.jpg")
    proxy = ProxyImagen(imagen_real)

    # La imagen real se carga y muestra solo cuando se llama a mostrar en el proxy.
    proxy.mostrar()
    print("-----------------------")
    proxy.mostrar()
