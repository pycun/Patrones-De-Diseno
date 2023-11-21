from abc import ABC, abstractmethod

class Internet(ABC):
    @abstractmethod
    def connect_to(self, host):
        pass

class ProxyInternet(Internet):

    banned_sites = ["banned.com"]

    def __init__(self):
        self.internet = RealInternet()

    def connect_to(self, host):
        if host in self.banned_sites:
            print("Acceso denegado a " + host)
            return
        self.internet.connect_to(host)

class RealInternet(Internet):
    def connect_to(self, host):
        print("Conexión exitosa a " + host)

if __name__ == "__main__":
    proxy = ProxyInternet()
    proxy.connect_to("example.com")
    proxy.connect_to("banned.com")
