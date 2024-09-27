from veiculo import Carro, Moto, Caminhao
from entrada_dados import obter_dados_veiculo, obter_dados_carro, obter_dados_moto, obter_dados_caminhao, obter_tipo_veiculo

# Lógica principal
marca, modelo, ano, cor = obter_dados_veiculo()
tipo_veiculo = obter_tipo_veiculo()

if tipo_veiculo == "carro":
    num_portas = obter_dados_carro()
    veiculo_usuario = Carro(marca, modelo, ano, cor, num_portas)
elif tipo_veiculo == "moto":
    tipo = obter_dados_moto()
    veiculo_usuario = Moto(marca, modelo, ano, cor, tipo)
elif tipo_veiculo == "caminhao":
    carga_maxima = obter_dados_caminhao()
    veiculo_usuario = Caminhao(marca, modelo, ano, cor, carga_maxima)
else:
    print("Tipo de veículo inválido. Encerrando o programa.")
    exit()

# Exibir informações do veículo
print("\nInformações do Veículo:")
veiculo_usuario.exibir_informacoes()
