
def calcular_custo_funeral():
    idade = int(input("Por favor, insira a idade do falecido: "))
    tipo_caixao = input("Por favor, insira o tipo de caixão (luxo, medio, basico): ")
    quer_flores = input("A família quer flores? (sim/nao): ")

    custo_base = 1000
    custo_caixao = 0
    custo_flores = 0

    if idade < 50:
        custo_base += 500
    elif idade >= 50 and idade < 70:
        custo_base += 1000
    else:
        custo_base += 1500

    if tipo_caixao == 'luxo':
        custo_caixao = 2000
    elif tipo_caixao == 'medio':
        custo_caixao = 1000
    else:
        custo_caixao = 500

    if quer_flores == 'sim':
        custo_flores = 200

    custo_total = custo_base + custo_caixao + custo_flores
    print("O custo total do funeral é: ", custo_total)

calcular_custo_funeral()