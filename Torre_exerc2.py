def verificar_prescricao():
    medicamentos_prescricao = ['morfina', 'oxycodona', 'metadona', 'fentanil']  

    nome_medicamento = input("Insira o nome do medicamento: ")

    if nome_medicamento.lower() in medicamentos_prescricao:
        print("O medicamento", nome_medicamento, "requer prescrição médica.")
        return True
    else:
        print("O medicamento", nome_medicamento, "não requer prescrição médica.")
        return False

verificar_prescricao()
