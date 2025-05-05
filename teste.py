def calcular_preco_final(preco_porta, desconto, vpl, il, rateio_vpl, icms):
    """
    Calcula o preço final de um produto considerando:
    - Desconto comercial aplicado ao preço da porta
    - Custo rateado do VPL
    - Imposto local (IL)
    - ICMS sobre o preço bruto final
    """
    preco_com_desconto = preco_porta * (1 - desconto)
    custo_vpl_rateado = vpl * rateio_vpl
    preco_bruto = preco_com_desconto + custo_vpl_rateado + il
    preco_final = preco_bruto / (1 - icms)

    return {
        "Preço com desconto": round(preco_com_desconto, 2),
        "Custo VPL rateado": round(custo_vpl_rateado, 2),
        "Preço bruto": round(preco_bruto, 2),
        "Preço final com ICMS": round(preco_final, 2)
    }


def main():
    print("Calculadora de Preço Final com Desconto, VPL e ICMS")
    preco_porta = float(input("Informe o preço da porta: R$ "))
    desconto = float(input("Informe o desconto comercial (ex: 0.05 para 5%): "))
    vpl = float(input("Informe o valor total do VPL: R$ "))
    il = float(input("Informe o valor do imposto local (IL): R$ "))
    rateio_vpl = float(input("Informe o percentual de rateio do VPL (ex: 0.01 para 1%): "))
    icms = float(input("Informe o percentual de ICMS (ex: 0.17 para 17%): "))

    resultado = calcular_preco_final(preco_porta, desconto, vpl, il, rateio_vpl, icms)

    print("\n--- Resultado ---")
    for chave, valor in resultado.items():
        print(f"{chave}: R$ {valor:.2f}")


if __name__ == "__main__":
    main()
