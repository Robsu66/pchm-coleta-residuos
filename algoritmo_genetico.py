from utils import calcular_custo_total
import random

def montar_caminho(indice_garagem, cromossomo, indice_lixao):
    return [indice_garagem] + cromossomo + [indice_lixao]

def gerar_população_inicial(pontos_intermediarios, tamanho_populacao):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_intermediarios[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

def selecao_torneio(populacao, custos, tamanho_torneio):
    indices_candidatos = random.sample(range(len(populacao)), tamanho_torneio)
    melhor_indice = min(indices_candidatos, key=lambda i: custos[i])
    return populacao[melhor_indice][:]

def cruzamento_ox(pai1, pai2):
    tamanho = len(pai1)
    ponto_a, ponto_b = sorted(random.sample(range(tamanho), 2))
    filho = [None] * tamanho
    filho[ponto_a:ponto_b+1] = pai1[ponto_a:ponto_b+1]
    genes_usados = set(filho[ponto_a:ponto_b+1])

    posicao_filho = (ponto_b + 1) % tamanho
    posicao_pai2 = (ponto_b + 1) % tamanho

    while None in filho:
        gene = pai2[posicao_pai2]
        if gene not in genes_usados:
            filho[posicao_filho] = gene
            genes_usados.add(gene)
            posicao_filho = (posicao_filho + 1) % tamanho
        posicao_pai2 = (posicao_pai2 + 1) % tamanho
    return filho

def mutacao_troca(cromossomo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(cromossomo)), 2)
        cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]
    return cromossomo

def rota_algoritmo_genetico(matriz_custo, nomes_pontos, indice_garagem, indice_lixao,
                            tamanho_populacao=100, geracoes = 300, tamanho_torneio = 3, elitismo = 2, 
                            taxa_mutacao = 0.1, semente = None):
    if semente is not None:
        random.seed(semente)

    pontos_intermediarios = [i for i in range(len(matriz_custo)) 
                            if i != indice_garagem and i !=indice_lixao]

    populacao = gerar_população_inicial(pontos_intermediarios, tamanho_populacao)
    melhor_cromossomo_global = None
    melhor_custo_global = float("inf")

    for _ in range(geracoes):
        custos = [calcular_custo_total(matriz_custo, montar_caminho(indice_garagem, ind, indice_lixao))
            for ind in populacao]

        indice_melhor = min(range(len(populacao)), key=lambda i: custos[i])
        if custos[indice_melhor] < melhor_custo_global:
            melhor_custo_global = custos[indice_melhor]
            melhor_cromossomo_global = populacao[indice_melhor][:]

        indices_ordenados = sorted(range(len(populacao)), key = lambda i:custos[i])
        nova_populacao = [populacao[i][:] for i in indices_ordenados[:elitismo]]

        while len(nova_populacao) < tamanho_populacao:
            pai1 = selecao_torneio(populacao, custos, tamanho_torneio)
            pai2 = selecao_torneio(populacao, custos, tamanho_torneio)
            filho = mutacao_troca(cruzamento_ox(pai1, pai2), taxa_mutacao)
            nova_populacao.append(filho)

        populacao = nova_populacao
    
    caminho = montar_caminho(indice_garagem, melhor_cromossomo_global, indice_lixao)
    custo_total = melhor_custo_global

    print("Rota sugerida (Algoritmo Genético):", [nomes_pontos[i] for i in caminho])
    return caminho, custo_total