from produtos import *
def menu():
  while True:
      print("\nMenu:")
      print("1- Verificar estoque")
      print("2- Realizar venda")
      print("3- Sair")
      opcao = int(input("Escolha uma opção: "))

      if opcao == 1:
          print("Estoque atual:")
          print(f"acai_banana: {acai_banana.verificar_estoque()} unidades")
          print(f"acai_morango: {acai_morango.verificar_estoque()} unidades")
          print(f"acai_granola: {acai_granola.verificar_estoque()} unidades")
      elif opcao == 2:
          produto = input("Digite o nome do produto que deseja comprar: ")
          quantidade = int(input("Digite a quantidade que deseja comprar: "))
          if produto == 'acai_banana':
              if acai_banana.realizar_venda(quantidade):
                 print("Compra realizada com sucesso!")
              else:
                 print("Estoque insuficiente!")
          elif produto == 'acai_morango':
              if acai_morango.realizar_venda(quantidade):
                 print("Compra realizada com sucesso!")
              else:
                 print("Estoque insuficiente!")
          elif produto == 'acai_granola':
              if acai_granola.realizar_venda(quantidade):
                 print("Compra realizada com sucesso!")
              else:
                 print("Estoque insuficiente!")
          else:
              print("Produto não encontrado!")
      elif opcao == 3:
          break
      else:
          print("Opção inválida!")
menu()