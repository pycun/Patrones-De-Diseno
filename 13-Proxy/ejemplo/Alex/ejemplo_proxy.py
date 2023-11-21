import os
from abc import ABC, abstractmethod

class Servidor(ABC):
    @abstractmethod
    def descargar(self, url):
        pass

class MiServidor(Servidor):
    def __init__(self, p, h):
        self.puerto = p
        self.host = h
    def descargar(self, url):
        return "Descargando para " + self.host
    
class ProxyMiServidor(Servidor):
    def __init__(self, p, h):
        self.puerto = p
        self.host = h
        self.miservidor = None
    def descargar(self, url):
        if(self.validar(url)):
            if(self.miservidor == None):
                self.miservidor = MiServidor(self.puerto, self.host)
            resultado = self.miservidor.descargar(url)
        else:
            resultado = "Desde " + self.host + " no puedes descargar"
        return resultado
    def validar(self, url):
        if (url == "/home/leonardo/Escritorio/ejemplo/Bob"):
            return True
        return False

path = os.getcwd()
program = ProxyMiServidor(6666, "Alex")
print(path)
result = program.descargar(path)
print(result)
