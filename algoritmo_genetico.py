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
    if random.random() > taxa_mutacao:
        i, j = random.sample(range(len(cromossomo)), 2)
        cromossomo[i], cromossomo[j] = cromossomo[j],
        cromossomo[i]
    return cromossomo