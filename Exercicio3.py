"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json


with open('dados.json', 'r') as dados:
    dados_dict = json.load(dados)

# print(dados_dict)

menor_valor = 99999999999999999999999999
dia_menor_valor = 0

maior_valor = 0
dia_maior_valor = 0

dias_uteis = 0
soma_valor_mes = 0
media_mensal = 0




for diaria in dados_dict:
    if diaria["valor"] != 0:

        dias_uteis += 1

        soma_valor_mes += diaria["valor"]


        if menor_valor > diaria["valor"]:
            menor_valor = diaria["valor"]
            dia_menor_valor = diaria["dia"]

        if maior_valor < diaria["valor"]:
            maior_valor = diaria["valor"]
            dia_maior_valor = diaria["dia"]

media_mensal = soma_valor_mes / dias_uteis

quantidade_dias_acima_media = 0

for diaria in dados_dict:
    if diaria["valor"] >= media_mensal:
        quantidade_dias_acima_media += 1

   
print("O menor valor é:", menor_valor, "no dia", dia_menor_valor) 
print("E o maior valor é:", maior_valor, "no dia", dia_maior_valor)

print("A média mensal contando apenas os dias úteis é de:", media_mensal)
print("São", dias_uteis, "dias úteis no mes, dentre eles a quantidade de dias em que o faturamento foi superior a média mensal é de:", quantidade_dias_acima_media)