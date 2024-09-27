def obter_dados_veiculo():
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))
    cor = input("Digite a cor do veículo: ")
    return marca, modelo, ano, cor


def obter_dados_carro():
    num_portas = int(input("Digite o número de portas do carro: "))
    return num_portas


def obter_dados_moto():
    tipo = input("Digite o tipo da moto: ")
    return tipo


def obter_dados_caminhao():
    carga_maxima = float(input("Digite a carga máxima do caminhão (em toneladas): "))
    return carga_maxima


def obter_tipo_veiculo():
    return input("Escolha o tipo de veículo (carro, moto ou caminhao): ")
