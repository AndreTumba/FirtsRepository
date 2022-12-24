
class Carro():
    numrodas = 4
    numbancos = 4
    veloc = 0
    acel = 20
    som = "Vruum!"
    p = 0

    def acelCarro(self, acel=20):
        self.veloc += acel

    def freiaCarro(self):
        if self.veloc > 20:
            self.veloc = self.p
        else:
            self.veloc = self.p

    def dimiAcel(self):
        if self.veloc > 20:
            self.veloc = 0

    def mostrarSom(self):
        print(self.som)


tracker = Carro()
ferrari = Carro()
ferrari.som = "vRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUM"
ferrari.mostrarSom()
tracker.mostrarSom()
tracker.acelCarro()
ferrari.veloc = 50
ferrari.acelCarro(40)
ferrari.freiaCarro()
print(ferrari.veloc)
tracker.acelCarro(50)
print(tracker.veloc)