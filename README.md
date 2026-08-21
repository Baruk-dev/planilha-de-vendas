# planilha-de-vendas

## Desafio

Construir um aplicativo simples que leia os dados, processe e exiba resultados organizados. O programa deve ser em Python e precisa:

declarar uma matriz 2D representando vendas;

* calcular totais por vendedor;
* calcular totais por mês;
* calcular o total geral;
* identificar o melhor vendedor.

Etapa 1 – Exibição organizada
Percorra a matriz e exiba os valores organizados por vendedor. Analise e responda:

* Quantas linhas existem?

  * R.: 3
* Quantas colunas existem?

  * R.: 3

Etapa 2 – Total por vendedor
Calcule o total vendido por cada vendedor. Para isso: utilize laços aninhados; reinicie o acumulador para cada linha.

Ele deve exibir:

* total vendedor 0;
* total vendedor 1;
* total vendedor 2.

Etapa 3 – Total por mês
Agora, calcule o total vendido em cada mês. Para isso: inverta a lógica dos laços; percorra colunas primeiro.

Ele deve exibir:

* total mês 0;
* total mês 1;
* total mês 2.

Etapa 4 – Total geral
Calcule o total geral da empresa.

Etapa 5 – Melhor vendedor
Identifique qual vendedor obteve maior total de vendas. Ele deve exibir:

o melhor vendedor.

Etapa 6 – Texto explicativo

* Analise todos os passos realizados e responda:

* Como os laços aninhados foram utilizados?

  * R.: Foram utilizados para percorrer a matriz de vendas. O laço externo percorre os vendedores (linhas) e o laço interno percorre as vendas de cada vendedor (colunas), oque faz ele acessar todos os valores da matriz.

* Como foi feito o controle de índices?

  * R.: Com as variáveis i e j, o i representa o indice das linhas e o j o indice das colunas.

* Qual foi o resultado da análise?

  * R.: O resultado mostrou que o vendedor 0 teve um total de 3800 vendas, o vendedor 1 3700 vendas e o vendedor 2 4200 vendas, ao todo foi um total de 11700 vendas, e o melhor vendeor foi o 2 com 4200 vendas.
