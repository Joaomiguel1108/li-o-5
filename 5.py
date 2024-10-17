veiculo = float(input("Digite o preço de fabrica do veiculo"))
lucro = float(input("Digite o lucro do distribuidor"))
imposto = (input("Digite o valor em impostos"))

lucro_distribuidor = (lucro/100)*veiculo
imposto2 = (imposto/100)*veiculo'
preco_total = veiculo+lucro+imposto

print(f"O valor total do veiculo é {preco_total}")
