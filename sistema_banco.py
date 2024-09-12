menu = """
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
    print("Deposito")

    valor = int(input("Informe o valor a ser depositado: "))
    if valor > 0:
      saldo += valor
    else:
      print("Valor invalido, informe um novo valor valido." )
    print(saldo)



  elif opcao == "2":
    print("Saque")

  elif opcao == "3":
    print("Extrato")

  elif opcao == "0":
    print("Obrigado por utilizar nossos serviços. Volte Sempre!")
    break

  else:
    print("Operação invalida, por favor selecione novamente a operação desejada.")