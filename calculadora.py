def calcular_valor_com_desconto(valor_original, desconto, icms_percentual):
    """
    Aplica o desconto comercial e reaplica o ICMS.
    """
    base_sem_imposto = valor_original / (1 + icms_percentual / 100)
    base_com_desconto = base_sem_imposto * (1 - desconto / 100)
    valor_final = base_com_desconto * (1 + icms_percentual / 100)
    return valor_final

def encontrar_desconto_para_valor_desejado(valor_original, valor_desejado, icms_percentual, precisao=0.01):
    """
    Utiliza busca binária para encontrar o desconto necessário para atingir o valor desejado.
    """
    inicio = 0
    fim = 100
    while fim - inicio > precisao:
        meio = (inicio + fim) / 2
        valor_calculado = calcular_valor_com_desconto(valor_original, meio, icms_percentual)

        if valor_calculado > valor_desejado:
            inicio = meio
        else:
            fim = meio
    return round(meio, 2)

def main():
    print("=== CALCULADORA DE DESCONTO NECESSÁRIO ===")
    
    try:
        valor_original = float(input("Digite o valor original (com imposto): R$ ").replace(",", "."))
        valor_desejado = float(input("Digite o valor desejado (Price + Tax): R$ ").replace(",", "."))
        icms_percentual = float(input("Digite o percentual de ICMS (%): ").replace(",", "."))

        desconto_necessario = encontrar_desconto_para_valor_desejado(valor_original, valor_desejado, icms_percentual)

        print(f"\nDesconto necessário aproximado: {desconto_necessario:.2f}%")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números válidos.")

if __name__ == "__main__":
    main()
