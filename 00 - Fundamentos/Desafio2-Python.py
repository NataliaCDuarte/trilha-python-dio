menu = """
Escolha uma opção:
[d] Depósito
[s] Saque
[e] Ver Extrato
[q] Sair

Digite a opção desejada: """
    
saldo = 0
limite_saque = 500
extrato = ""
qtd_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao_usuario = input(menu)

    if  opcao_usuario == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.\n"
        else:
            print("Erro! O valor do depósito não pode ser negativo ou zero.")

    elif opcao_usuario == "s":
        valor_saque = float(input("Digite o valor do saque: "))

        # Verificando se o saque é válido
        saldo_insuficiente = valor_saque > saldo
        limite_excedido = valor_saque > limite_saque
        max_saques_excedido = qtd_saques >= LIMITE_DE_SAQUES

        if saldo_insuficiente:
            print("Erro! Saldo insuficiente para o saque.")
        elif limite_excedido:
            print(f"Erro! O valor máximo para saque é de R$ {limite_saque:.2f}.")
        elif max_saques_excedido:
            print(f"Erro! Você já atingiu o limite de {LIMITE_DE_SAQUES} saques.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque:.2f} realizado.\n"
            qtd_saques += 1
        else:
            print("Erro! O valor do saque deve ser positivo.")

    elif opcao_usuario == "e":
        print("\n=============== EXTRATO ===============")
        if not extrato:
            print("Nenhuma movimentação registrada.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao_usuario == "q":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
