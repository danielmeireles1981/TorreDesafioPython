def verificar_socios():
    socios = ['João', 'Maria', 'Carlos', 'Ana']  # Exemplo de lista de sócios
    nomes_visitantes = []

    while True:
        nome = input("Insira o nome do visitante (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        nomes_visitantes.append(nome)

    nomes_socios = [nome for nome in nomes_visitantes if nome in socios]
    print("Os seguintes visitantes são sócios: ", nomes_socios)


verificar_socios()
