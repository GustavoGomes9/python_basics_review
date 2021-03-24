class Cars:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f'Carro ligado!!'
    
    def define_carro(self):
        return f'Seu carro é da marca: {self.marca}'

c = Cars('ford','2019','prata')
print(c.ligar())
print(c.define_carro())