depósito = float(input("Digite o valor do depósito"))
juros = float(input("Digite o valor dos juros"))
tempo = int(input("Digite quantos meses o valor ficara depositado"))

calculo1 = ((depósito/100)*juros)*tempo


total = depósito+calculo1

print(f"O valor do seu depósito depois de {tempo} meses, é {total}")
