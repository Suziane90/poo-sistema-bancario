from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
    def __init__(self,numero):
        self._numero = numero
        self._saldo = 0
    @property
    @abstractmethod
    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero