class Produto:
   def __init__(self, nome, quantidade_estoque, valor):
       self.nome = nome
       self.quantidade_estoque = quantidade_estoque
       self.valor = valor

   def verificar_estoque(self):
       return self.quantidade_estoque

   def realizar_venda(self, quantidade):
       if self.quantidade_estoque >= quantidade:
           self.quantidade_estoque -= quantidade
           return True
       else:
           return False
acai_banana = Produto('acai_banana', 20, 15.00)
acai_morango = Produto('acai_morango', 15, 25.00)
acai_granola = Produto('acai_granola', 35, 17.00)
