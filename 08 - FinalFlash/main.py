# Main.py
from Profissional import Profissional
from PacoteFotos import PacoteFotos
from EstudioFotografia import EstudioFotografia

# Obter entrada de dados do usuário
nomeProfissional = input("Digite o nome do profissional: ")
quantidadeFotos = int(input("Digite a quantidade de fotos desejadas: "))
tamanhoFotos = input("Digite o tamanho desejado das fotos: ")
horarioEntrega = input("Digite o horário desejado para a entrega: ")

# Criar instâncias com base nos dados do usuário
fotografo = Profissional(nomeProfissional)
pacote = PacoteFotos(quantidadeFotos, tamanhoFotos)

# Agendar a sessão com os dados fornecidos pelo usuário
estudio = EstudioFotografia()
sessaoAgendada = estudio.agendarSessao(fotografo, pacote, horarioEntrega)

# Exibir informações
print(f"Sessão agendada com {sessaoAgendada.profissional.nome} para as {horarioEntrega}.")
print(f"Pacote de fotos: {sessaoAgendada.pacoteFotos.quantidade} fotos no tamanho {sessaoAgendada.pacoteFotos.tamanho}.")
print(f"Entrega programada para as {sessaoAgendada.horarioEntrega}.")