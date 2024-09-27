def calcular_total_pedido():
    itens_pedido = []
    while True:
        item = input("Insira o nome do item (ou 'sair' para finalizar o pedido): ")
        if item.lower() == 'sair':
            break
        preco = float(input("Insira o preço do item: "))
        itens_pedido.append({'nome': item, 'preco': preco})

    total = 0
    for item in itens_pedido:
        total += item['preco']

    print("O total do pedido é: ", total)

calcular_total_pedido()
