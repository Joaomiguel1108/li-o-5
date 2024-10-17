conta = 0
conta = valor
valor = float(input("Digite o valor depositado"))
valor_cheque1 = float(input("Digite do primeiro cheque"))
valor_cheque2 = float(input("Digite do segundo cheque"))

cheque1 = ((valor_cheque1/100)*0.38
cheque2 = ((valor_cheque2/100)*0.38

conta = conta - (cheque2+cheque1)

print(f"O seu saldo atual é {conta}")
