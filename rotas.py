import random
import math

# -----------------------------
# Cidades (x, y)
# -----------------------------
cidades = [
    (0, 0),
    (1, 5),
    (5, 2),
    (6, 6),
    (8, 3)
]

# -----------------------------
# Distância entre duas cidades
# -----------------------------
def distancia(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# -----------------------------
# Fitness (quanto menor melhor)
# -----------------------------
def fitness(rota):
    total = 0
    for i in range(len(rota)):
        cidade_atual = cidades[rota[i]]
        proxima = cidades[rota[(i+1) % len(rota)]]
        total += distancia(cidade_atual, proxima)
    return total

# -----------------------------
# Criar população inicial
# -----------------------------
def criar_populacao(tamanho):
    populacao = []
    for _ in range(tamanho):
        rota = list(range(len(cidades)))
        random.shuffle(rota)
        populacao.append(rota)
    return populacao

# -----------------------------
# Seleção (torneio)
# -----------------------------
def selecao(pop):
    a, b = random.sample(pop, 2)
    return a if fitness(a) < fitness(b) else b

# -----------------------------
# Crossover (ordem)
# -----------------------------
def crossover(pai1, pai2):
    inicio, fim = sorted(random.sample(range(len(pai1)), 2))
    filho = [-1] * len(pai1)
    filho[inicio:fim] = pai1[inicio:fim]

    pos = 0
    for gene in pai2:
        if gene not in filho:
            while filho[pos] != -1:
                pos += 1
            filho[pos] = gene
    return filho

# -----------------------------
# Mutação
# -----------------------------
def mutacao(rota, taxa=0.1):
    if random.random() < taxa:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    return rota

# -----------------------------
# Algoritmo Genético
# -----------------------------
def algoritmo_genetico(geracoes=100, tamanho_pop=20):
    pop = criar_populacao(tamanho_pop)

    for g in range(geracoes):
        nova_pop = []
        for _ in range(tamanho_pop):
            p1 = selecao(pop)
            p2 = selecao(pop)
            filho = crossover(p1, p2)
            filho = mutacao(filho)
            nova_pop.append(filho)

        pop = sorted(nova_pop, key=fitness)

    melhor = pop[0]
    return melhor, fitness(melhor)

# -----------------------------
# Executar
# -----------------------------
melhor_rota, distancia_total = algoritmo_genetico()

print("Melhor rota:", melhor_rota)
print("Distância total:", distancia_total)