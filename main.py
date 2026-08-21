vendas = [[1200, 1500, 1100], [1000, 1300, 1400], [900, 1700, 1600]]

for i in range(len(vendas)):
    print(f"Vendedor {i}: ")
    for j in range(len(vendas[i])):
        print(f"{vendas[i][j]} ")
    print()

print("\nTotal de linhas: ", len(vendas))
print("Total de colunas: ", len(vendas[0]))

totais_vendedores = []
for i in range(len(vendas)):
    total = 0
    for j in range(len(vendas[i])):
        total += vendas[i][j]
    totais_vendedores.append(total)
    print(f"Total Vendedor {i}: {total}")

print("\nTotal do mês:")
for coluna in range(len(vendas[0])):
    total_mes = 0
    for linha in range(len(vendas)):
        total_mes += vendas[linha][coluna]
    print(f"Total do mês {coluna}: {total_mes}")

total_geral = 0
for linha in vendas:
    for valor in linha:
        total_geral += valor

print(f"\nTotal geral: {total_geral}")

melhor_vendedor = 0
maior_total = totais_vendedores[0]

for i in range(1, len(totais_vendedores)):
    if totais_vendedores[i] > maior_total:
        maior_total = totais_vendedores[i]
        melhor_vendedor = i

print(f"\nMelhor vendedor: Vendedor {melhor_vendedor}")
print(f"Total de vendas do melhor vendedor: {maior_total}")