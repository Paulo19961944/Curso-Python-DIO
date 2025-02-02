saldo = 2000
saque = float(input("Digite a quantidade que deseja sacar: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao Realizar o Saque!")