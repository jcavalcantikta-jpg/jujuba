class Produto:
    def __init__(self,nome, categoria, preço, estoque):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço
        self.estoque = estoque

    def exibir(self):
        print(f"Produto : {self.nome}")
        print(f"Categoria : {self.categoria}")
        print(f"Preço : {self.estoque}")


    def valor_total(self):
        return self.preço  * self.estoque

    def aplicar_desconto(self,percentual):
        self.preço *= (1-percentual / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preço}")

    def vender(self,quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente!:")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} x {self.nome}.Estoque restante: {self.estoque}")


    def repor_estoque(self,quantidade):
       self.estoque += quantidade
       print(f"Novo estoque: {self.estoque} ")


p1 = Produto("Fubá", "Alimentos", 2.99,20)
p2 = Produto("Caneta", "Papelaria", 1.99,30)

p1.exibir()
p2.exibir()

p1.vender(5)
p2.aplicar_desconto(50)
p1.repor_estoque(20)

print(f"\nValor total em estoque - {p1.nome}: R$ {p1.valor_total():.2f}")

p1.exibir()
p2.exibir()
