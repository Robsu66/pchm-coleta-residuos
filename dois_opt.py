from utils import calcular_custo_total

def inverter_segmento(caminho, i, j):
    return caminho[:i] + caminho[i:j + 1][::-1] + caminho[j + 1:]

def rota_2opt(matriz_custo, caminho_inicial, nomes_pontos):
    melhor_caminho = caminho_inicial[:]
    melhor_custo = calcular_custo_total(matriz_custo, melhor_caminho)
    total_pontos = len(melhor_caminho)

    melhorou = True
    while melhorou:
        melhorou = False
        for i in range(1, total_pontos - 2):
            for j in range(i + 1, total_pontos - 1):
                novo_caminho = inverter_segmento(melhor_caminho, i, j)
                novo_custo = calcular_custo_total(matriz_custo, novo_caminho)
                if novo_custo < melhor_custo:
                    melhor_caminho = novo_caminho
                    melhor_custo = novo_custo
                    melhorou = True

    print("Rota refinada (2-opt):", [nomes_pontos[i] for i in melhor_caminho])
    return melhor_caminho, melhor_custo