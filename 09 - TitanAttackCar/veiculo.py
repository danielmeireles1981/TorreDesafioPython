class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, num_portas):
        super().__init__(marca, modelo, ano, cor)
        self.num_portas = num_portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de Portas: {self.num_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, tipo):
        super().__init__(marca, modelo, ano, cor)
        self.tipo = tipo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo: {self.tipo}")


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cor, carga_maxima):
        super().__init__(marca, modelo, ano, cor)
        self.carga_maxima = carga_maxima

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Carga Máxima: {self.carga_maxima} toneladas")
