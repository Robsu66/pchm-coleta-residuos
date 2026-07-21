from utils import calcular_custo_total
import random

def montar_caminho(indice_garagem, cromossomo, indice_lixao):
    return [indice_garagem] + cromossomo + [indice_lixao]

def rota_algoritmo_genetico(matriz_distancias, nome_pontos, indice_garagem, indice_lixao):
    total_pontos = len(matriz_distancias)
    pontos_intermediarios = [i for i in range(total_pontos)
                              if i != indice_garagem and i != indice_lixao]
