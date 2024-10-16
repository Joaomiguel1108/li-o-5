import math

numero = float(input("Digite um numero maior que zero"))

calculo1 = numero**2
calculo2 = numero**3
calculo3 = math.sqrt(numero)
calculo4 = calculo3 ** (1/3)
print(f"O seu numero ao quadrado é {calculo1}, ao cubo é {calculo2}, a raiz quadrada dele é {calculo3}, e a raiz cubica é {calculo4} ")

if numero > 0:
    print("Numero invalido")
