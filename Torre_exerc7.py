class Procedimento:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class ClinicaEstetica:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.clientes = {}
        self.procedimentos = {'limpeza de pele': Procedimento('limpeza de pele', 100), 'massagem': Procedimento('massagem', 200), 'tratamento facial': Procedimento('tratamento facial', 300)}
        self.produtos = {'shampoo': 10, 'condicionador': 15, 'mascara de beleza': 20}
        self.pedidos = {}

    def agendar_consulta(self):
        cliente = input("Insira o nome do cliente: ")
        print("Procedimentos disponíveis: ", list(self.procedimentos.keys()))
        procedimento = input("Insira o procedimento: ")
        data = input("Insira a data (dd/mm/aaaa): ")
        self.clientes[cliente] = {'procedimento': self.procedimentos[procedimento], 'data': data}
        print(f"Procedimento {self.clientes[cliente]['procedimento'].nome} agendado para o cliente {cliente}.")

    def gerenciar_historico(self):
        cliente = input("Insira o nome do cliente: ")
        if cliente in self.clientes:
            print(f"Histórico de procedimentos para o cliente {cliente}: {self.clientes[cliente]['procedimento'].nome}")

    def fazer_pedido(self):
        print("Produtos disponíveis para compra: ", self.produtos)
        produto = input("Insira o nome do produto que deseja comprar: ")
        if produto in self.produtos:
            print(f"Pedido do produto {produto} realizado com sucesso!")
            self.pedidos[produto] = self.produtos[produto]
        else:
            print("Produto não disponível.")

    def gerar_relatorio(self):
        cliente = input("Insira o nome do cliente: ")
        if cliente in self.clientes:
            print(f"Relatório para o cliente {cliente}:")
            print(f"Clinica: {self.nome}")
            print(f"Endereço da clínica: {self.endereco}")
            print(f"Procedimentos realizados: {self.clientes[cliente]['procedimento'].nome}")
            print(f"Valor do procedimento: {self.clientes[cliente]['procedimento'].valor}")
            valor_produto = sum(self.pedidos.values())
            print(f"Valor do produto: {valor_produto}")
            print(f"Valor total: {self.clientes[cliente]['procedimento'].valor + valor_produto}")

    def menu(self):
        while True:
            print("\n1. Agendar consulta")
            print("2. Gerenciar histórico")
            print("3. Fazer pedido")
            print("4. Gerar relatório")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.agendar_consulta()
            elif opcao == '2':
                self.gerenciar_historico()
            elif opcao == '3':
                self.fazer_pedido()
            elif opcao == '4':
                self.gerar_relatorio()
            elif opcao == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso:
clinica = ClinicaEstetica('Beleza Pura', 'Rua das Flores, 123')
clinica.menu()
