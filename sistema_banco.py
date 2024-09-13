menu = """
===========================================

Olá, seja bem-vindo(a),
selecione a operação que deseja realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":
    print("========== Deposito ==========")

    valor = float(input("Informe o valor a ser depositado: "))
    if valor > 0:
      saldo += valor
      extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
      print("Valor inválido, informe um novo valor válido.")
    print(f"Saldo = R$ {saldo:.2f}")

  elif opcao == "2":
    print("========== Saque ==========")
    saque = float(
      input('''
  O limite por saque é de R$ 500,00 com limite de 3 saques diários.
  Informe o valor do saque.
  => '''))

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if saque > limite:
      print('''
  O valor informado passa do limite por operação.
  Informe um valor válido.
  ''')
    elif saque < 0:
      print("\nFalha na operação.\nInforme um valor válido.\n")
    elif saque > saldo:
      print("\nSaldo insuficiente para saque.")
    elif excedeu_saques:
      print("\nOperação falhou! Número máximo de saques excedido.")
    else:
      saldo -= saque
      extrato += f"Saque: R$ {saque:.2f}\n"
      numero_saques += 1

    print(f"  Saldo = R$ {saldo:.2f}")

  elif opcao == "3":
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: {saldo:.2f}\n")
    #print("=========================================")

  elif opcao == "0":
    print("\n==================================================")
    print("\nObrigado por utilizar nossos serviços. Volte Sempre!")
    print("\n==================================================")
    break

  else:
    print("Operação invalida, por favor selecione novamente a operação desejada.")