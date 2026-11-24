class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max


    def mover(self):
        print(f"O veículo da marca {self.marca} está se movendo "
              f"(velocidade máxima: {self.velocidade_max} km/h).")




class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas


    def mover(self):
        print(f"O carro {self.marca} de {self.num_portas} portas está "
              f"acelerando na estrada até {self.velocidade_max} km/h.")




class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas


    def mover(self):
        print(f"A bicicleta {self.marca} com {self.num_marchas} marchas "
              f"está sendo pedalada a até {self.velocidade_max} km/h.")


if __name__ == "__main__":
    veiculo = Veiculo("Genérica", 100)
    carro = Carro("Toyota", 180, 4)
    bicicleta = Bicicleta("Caloi", 40, 21)


    for v in (veiculo, carro, bicicleta):
        v.mover()


    print(isinstance(carro, Veiculo))      
    print(isinstance(bicicleta, Veiculo))