import numpy as np
from dados_matriz import matriz_distancias, matriz_tempo, nomes_pontos
from vizinho_mais_proximo import rota_vizinho_mais_proximo
from cheapest_insertion import rota_aresta_mais_baratas
from algoritmo_genetico import rota_algoritmo_genetico
from dois_opt import rota_2opt
from utils import calcular_custo_total

# Índices fixos
indice_garagem = nomes_pontos.index("Garagem")
indice_lixao = nomes_pontos.index("Lixão")

print("===== HEURÍSTICAS COM FOCO EM DISTÂNCIA =====\n")

# Vizinho mais próximo com foco em distância
caminho_vm, dist_vm = rota_vizinho_mais_proximo(matriz_distancias, nomes_pontos, indice_garagem, indice_lixao)
tempo_vm = calcular_custo_total(matriz_tempo, caminho_vm)
print(f"Distância: {dist_vm} metros | Tempo: {tempo_vm} segundos\n")

# Aresta mais barata com foco em distância
caminho_ab, dist_ab = rota_aresta_mais_baratas(matriz_distancias, nomes_pontos, indice_garagem, indice_lixao)
tempo_ab = calcular_custo_total(matriz_tempo, caminho_ab)
print(f"Distância: {dist_ab} metros | Tempo: {tempo_ab} segundos\n")

caminho_ab, dist_ab = rota_2opt(matriz_distancias, caminho_ab, nomes_pontos)
tempo_ab = calcular_custo_total(matriz_tempo, caminho_ab)
print(f"Distância: {dist_ab} metros | Tempo: {tempo_ab} segundos\n")

# Algoritmo genético com foco em distância
caminho_ag, dist_ag = rota_algoritmo_genetico(matriz_distancias, nomes_pontos, indice_garagem, indice_lixao)
tempo_ag = calcular_custo_total(matriz_tempo, caminho_ag)
print(f"Distância: {dist_ag} metros | Tempo: {tempo_ag} segundos\n")

caminho_ag, dist_ag = rota_2opt(matriz_distancias, caminho_ag, nomes_pontos)
tempo_ag = calcular_custo_total(matriz_tempo, caminho_ag)
print(f"Distância: {dist_ag} metros | Tempo: {tempo_ag} segundos\n")

print("\n\n")

print("===== HEURÍSTICAS COM FOCO EM TEMPO =====\n")

# Vizinho mais próximo com foco em tempo
caminho_vm_t, tempo_vm_t = rota_vizinho_mais_proximo(matriz_tempo, nomes_pontos, indice_garagem, indice_lixao)
dist_vm_t = calcular_custo_total(matriz_distancias, caminho_vm_t)
print(f"Tempo: {tempo_vm_t} segundos | Distância: {dist_vm_t} metros\n")

# Aresta mais barata com foco em tempo
caminho_ab_t, tempo_ab_t = rota_aresta_mais_baratas(matriz_tempo, nomes_pontos, indice_garagem, indice_lixao)
dist_ab_t = calcular_custo_total(matriz_distancias, caminho_ab_t)
print(f"Tempo: {tempo_ab_t} segundos | Distância: {dist_ab_t} metros\n")
