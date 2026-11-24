class Figura:
    def calcular_area(self):
        raise NotImplementedError("As subclasses devem implementar calcular_area().")


class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio


    def calcular_area(self):
        return math.pi * self.raio**2


figuras = [Retangulo(5, 3), Circulo(2), Retangulo(4, 6)]
areas = [figura.calcular_area() for figura in figuras]


for figura, area in zip(figuras, areas):
    print(f"Área de {figura.__class__.__name__}: {area:.2f}")