from Profissional import Profissional
from PacoteFotos import PacoteFotos
from SessaoFotos import SessaoFotos

class EstudioFotografia:
    def agendarSessao(self, profissional, pacoteFotos, horarioEntrega):
        sessao = SessaoFotos(profissional, pacoteFotos, horarioEntrega)
        return sessao