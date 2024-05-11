menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        if saque >= 500:
            print("O limite máximo de saque é 500 reais")
        elif saque > saldo:
            print("Não será possivel sacar, por insuficiencia de saldo")
        elif numero_saques <= LIMITE_SAQUES:
            ++numero_saques
            saldo = saldo - saque
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("você atingiu o limite de saque diário")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")
