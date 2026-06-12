import random
import networkx as nx
import pandas as pd
import numpy as np

def random_subset(repeated_nodes, m):
    targets = set()
    while len(targets) < m:
        targets.add(random.choice(repeated_nodes))
    return list(targets)

def barabasi_albert_com_custo(n, m, seed=None):
    """
    Gera um grafo simples e conexo (n nós) via Barabási-Albert,
    aplicando pesos aleatórios entre [1, 20] nas arestas.
    """
    if m < 1 or m >= n:
        raise ValueError("O parâmetro m deve ser >= 1 e < n.")
    if seed is not None:
        random.seed(seed)
        
    G = nx.Graph()
    
    # Cria o núcleo inicial conexo para garantir que todo o grafo final seja conexo
    G.add_nodes_from(range(m))
    for i in range(m):
        for j in range(i + 1, m):
            G.add_edge(i, j, weight=random.randint(1, 20))
            
    repeated_nodes = list(range(m)) * m
    
    # Preferential attachment
    for source in range(m, n):
        targets = random_subset(repeated_nodes, m)
        for t in targets:
            G.add_edge(source, t, weight=random.randint(1, 20))
            
        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * m)
        
    return G

def extrair_matrizes(G):
    """
    Gera e retorna a matriz de adjacência e a matriz de custo.
    """
    nodes = sorted(G.nodes())
    
    # Matriz de Adjacência (Apenas 0 e 1 indicando conectividade)
    adj_matrix = nx.to_numpy_array(G, nodelist=nodes, weight=None, dtype=int)
    df_adj = pd.DataFrame(adj_matrix, index=nodes, columns=nodes)
    
    # Matriz de Custo (Valores de 1 a 20 onde há aresta, 0 onde não há)
    cost_matrix = nx.to_numpy_array(G, nodelist=nodes, weight='weight', dtype=int)
    df_cost = pd.DataFrame(cost_matrix, index=nodes, columns=nodes)
    
    return df_adj, df_cost