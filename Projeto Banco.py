menu = """
   MENU

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o quanto quer depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito : R$ {deposito:.2f}\n'
            print(f"Depósito realizado com sucesso. Seu saldo agora é: {saldo}")
        else:
            print("So pode depositar saldo positivo!")
    elif opcao == 2:
        saque = (float(input("Digite o quanto quer sacar: ")))
        excedeu_saque = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        if excedeu_saque:
            print(f"Saque não realizado. Você não tem saldo suficiente. Saldo disponível no momento é de: {saldo}")
        elif excedeu_limite:
            print("Saque não realizado. O limite para saque é de R$ 500,00")
        elif excedeu_saques:
            print('Limite de saques digiários atingidos.')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numeros_saques += 1
            print(f'Saque realizado com sucesso. Seu saldo agora é: {saldo}')
    elif opcao == 3:
        print(' Não foram realizadas movimentaçoes.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
    elif opcao == 0:
        print('Ok, fechando...')
        break
    else:
        print("Opção inválida. Por favor, selecione o opção desejada")
        

        