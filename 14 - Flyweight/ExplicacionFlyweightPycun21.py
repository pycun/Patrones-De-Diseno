import time

from memory_profiler import profile
from pympler import asizeof

class LibroFlyweight:
    """ Flyweight que representa el contenido compartido de un libro (Intrinseco). Es inmutable debido a que no hay un metodo que actualice los valores"""
    def __init__(self, _id, nombre, autor, contenido):
        self._id = _id
        self.nombre = nombre
        self.autor = autor
        self.contenido = contenido

class LibroFactory:
    """ Fábrica Flyweight para crear o reutilizar instancias de LibroFlyweight. """
    _libros_flyweight = {}
	
    @classmethod
    def get_key(cls, data):
        """
        Devuelve un string que sera la llave del diccionario
        """

        return "_".join(sorted(data))

    @classmethod
    def obtener_flyweight(cls, _id, nombre, autor, contenido):
        key = cls.get_key([_id, nombre, autor])  ## Importante explicar
        msg = ""
        if key not in cls._libros_flyweight:
            cls._libros_flyweight[key] = LibroFlyweight(_id, nombre, autor, contenido)
            size = asizeof.asizeof(cls._libros_flyweight[key])/1024**2
            msg = F"LibroFactory: No existe el LibroFlyweight, creando uno nuevo. Tamaño: {size}"
        else:
            msg = "LibroFactory: Reutilizando un LibroFlyweight existente."
            
        # Mostrar tamaño de la RAM?}
        print(msg)
        return cls._libros_flyweight[key]

class Libro:
    """ Clase de libro que mantiene su estado único (extrínseco). """
    def __init__(self, editorial, edicion, precio, _id, nombre, autor, contenido):
        self.editorial = editorial
        self.edicion = edicion
        self.precio = precio
        self.flyweight = LibroFactory.obtener_flyweight(_id, nombre, autor, contenido)

    def mostrar_informacion(self):
        """ Muestra la información completa del libro. """
        print(f"ID: {self.flyweight._id}, "
              f"Editorial: {self.editorial}, "
              f"Edicion: {self.edicion}, "
              f"Precio: {self.precio}",
              f"Nombre: {self.flyweight.nombre}, "
              f"Autor: {self.flyweight.autor}, "
              f"Contenido: {self.flyweight.contenido}, ")


@profile
def revisar_memoria():
    libro1 = Libro(
        "Porrua",
        "Edicion de Bolsillo",
        "100",
        "1000",
        "100 años de soledad",
        "Gabriel Garcia Marquez",
        "Muchos años después, frente al pelotón de fusilamiento ..."
    )

    libro2 = Libro(
        "Alfaguara",
        "Edicion Especial",
        "150",
        "2000",
        "100 años de soledad",
        "Gabriel Garcia Marquez",
        "Muchos años después, frente al pelotón de fusilamiento ..."
    )

    libro3 = Libro(
        "Santillana",
        "Edicion de Lujo",
        "200",
        "3000",
        "100 años de soledad",
        "Gabriel Garcia Marquez",
        "Muchos años después, frente al pelotón de fusilamiento ..."
    )

    libro4 = Libro(
        "Gandhi",
        "Edicion de Bolsillo",
        "80",
        "4000",
        "100 años de soledad",
        "Gabriel Garcia Marquez",
        "Muchos años después, frente al pelotón de fusilamiento ..."
    )

    libro5 = Libro(
        "Porrua",
        "Edicion de Especial",
        "120",
        "5000",
        "100 años de soledad",
        "Gabriel Garcia Marquez",
        "Muchos años después, frente al pelotón de fusilamiento ..."
    )

    libro6 = Libro(
        "Porrua",
        "Edicion de Especial",
        "200",
        "6000",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        [x for x in range(10000000)]
    )

    libro7 = Libro(
        "Ghandi",
        "Edicion de Especial",
        "200",
        "6000",
        "Don Quijote de la Mancha 2",
        "Miguel de Cervantes",
        [x for x in range(10000000)]
    )

    libro8 = Libro(
        "Alfaguara",
        "Edicion de Especial",
        "200",
        "6000",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        [x for x in range(10000000)]
    )

    libro9 = Libro(
        "Siglo 21",
        "Edicion de Especial",
        "200",
        "6000",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        [x for x in range(10000000)]
    )

    libro10 = Libro(
        "Centenario",
        "Edicion de Especial",
        "200",
        "6000",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        [x for x in range(10000000)]
    )

    libro1.mostrar_informacion()
    time.sleep(15)

revisar_memoria()