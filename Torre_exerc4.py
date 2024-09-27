def calcular_desconto():
    compras = []
    while True:
        item = input("Insira o nome do item (ou 'sair' para finalizar a compra): ")
        if item.lower() == 'sair':
            break
        valor = float(input("Insira o valor do item: "))
        compras.append({'nome': item, 'valor': valor})

    valor_total = sum(item['valor'] for item in compras)
    desconto = 0

    if valor_total > 100:
        desconto = 0.1  # 10% de desconto
    elif valor_total > 50:
        desconto = 0.05  # 5% de desconto
    else:
        desconto = 0  # sem desconto

    valor_desconto = valor_total * desconto
    valor_final = valor_total - valor_desconto
    print("O valor do desconto foi: ", valor_desconto)
    print("O valor final após o desconto é: ", valor_final)

calcular_desconto()
