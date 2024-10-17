horas = float(input("Digite quantas horas foram trabalhadas"))
minimo = float(input("Digite o valor do salario minimo"))

valor_hora = minimo/2
salario_bruto = horas*valor_hora
imposto = (salario_bruto/100)*3
salario = salario_bruto - imposto

print(f"O seu salario é {salario}")
