from conta import Conta

class ContaEspecial(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self._bonus = 0

    def renderBonus(self):
        super().creditar(self._bonus)
        self._bonus = 0

    def creditar(self, valor):
        self._bonus = self._bonus + (valor * 0.01)
        super().creditar(valor)

