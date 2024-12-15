def crescimento_percentual(vendas_mensais):
    # Extraia os valores de venda de dois meses:
    venda_mes_anterior = vendas_mensais[0]["valor_venda"]
    venda_mes_atual = vendas_mensais[1]["valor_venda"]
    
    # Calcule o crescimento percentual
    crescimento = ((venda_mes_atual - venda_mes_anterior) / venda_mes_anterior) * 100
    return crescimento

vendas_mensais = []

for i in range(2):
    mes = input()
    valor_venda = float(input())
    vendas_mensais.append({"mes": mes, "valor_venda": valor_venda})

# Chame a função e imprime o resultado:
resultado = crescimento_percentual(vendas_mensais)
print(f"Crescimento percentual de vendas: {resultado:.2f}%")

