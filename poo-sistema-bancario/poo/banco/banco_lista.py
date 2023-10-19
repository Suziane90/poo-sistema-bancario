from poo.conta.conta import Conta
from poo.conta.conta_abstrata import ContaAbstrata
from poo.conta.conta_poupanca import ContaPoupanca


class BancoLista(ContaAbstrata):

    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        origem = self.procurar_conta(origem)
        destino = self.procurar_conta(destino)

        if origem and destino:
            if self.saldo(origem.get_numero()) >= valor:
                origem.debitar(valor)
                destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo Insuficiente, faça um empréstimo")
        else:
            print("Sua transferência foi negada! Conta Inexistente!")

#aula 4: Herança

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            if isinstance(conta, ContaPoupanca):
                conta.render_juros(0.01)
                print("Saldo com juros: {}".format(conta.get_saldo()))
            else:
                print("Conta não é poupança!")