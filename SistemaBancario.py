#aqui esta apenas uma parte da logica 
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('informe o  valor de depósito: '))

        if valor > 0:
            saldo += valor 
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('valor informado inválido')

    elif opcao == 's':
        valor = float(input('informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('saldo insuficiente')

        elif excedeu_limite:
            print('o valor do saque excede seu limite')

        elif excedeu_saque:
            print('você não pode fazer mais de 3 saques')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {saldo:.2f}\n'
            numero_saques += 1

        else: 
            print('Valor informado inválido')

    elif opcao == 'e':
        print('\n=============== EXTRATO ===============') 
        print('não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo: .2f}')
        print('=========================================')

    elif opcao == 'q':
        break

    else:
        print('operação invalida')

        

