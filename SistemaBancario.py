#aqui esta apenas uma parte da logica 


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque ou valor inválido.')

    def extrato(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo atual: R${self.saldo}')



if __name__ == "__main__":
    
    conta = ContaBancaria('keli', 1000)

    
    conta.extrato()
    conta.deposito(500)
    conta.saque(200)
    conta.extrato()
