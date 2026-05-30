import random
import matplotlib.pyplot as plt
import networkx as nx
from degree_counter import count_node_degrees

def random_subset(repeated_nodes, m):
    """Escolhe m nós distintos com probabilidade proporcional ao grau."""
    targets = set()
    while len(targets) < m:
        targets.add(random.choice(repeated_nodes))
    return list(targets)

def barabasi_albert(n, m, seed=None):
    """
    Gera um grafo Barabási-Albert.
    
    n : número total de nós
    m : arestas que cada novo nó adiciona (1 <= m < n)
    """
    if m < 1 or m >= n:
        raise ValueError(f"Precisa: 1 <= m < n. Recebido m={m}, n={n}")
    
    if seed is not None:
        random.seed(seed)
    
    G = nx.Graph()
    
    # Começa com m nós isolados (núcleo inicial)
    G.add_nodes_from(range(m))
    
    # repeated_nodes: lista onde cada nó aparece uma vez por aresta
    # Isso implementa o "preferential attachment" — nós com mais
    # arestas aparecem mais vezes e têm maior chance de ser escolhidos
    repeated_nodes = []
    
    # Alvos iniciais para o primeiro novo nó
    targets = list(range(m))
    
    # Adiciona nós de m até n-1
    for source in range(m, n):
        # Liga o novo nó aos m alvos escolhidos
        G.add_edges_from((source, t) for t in targets)
        
        # Atualiza a lista: cada alvo ganha +1 aparição (recebeu aresta)
        repeated_nodes.extend(targets)
        # E o novo nó aparece m vezes (enviou m arestas)
        repeated_nodes.extend([source] * m)
        
        # Escolhe os próximos m alvos por preferential attachment
        targets = random_subset(repeated_nodes, m)
    
    return G


def visualize_barabasi(G, title="Barabási-Albert Network"):
    """
    Visualiza o grafo Barabási-Albert com os graus dos nós como labels.
    
    G : networkx.Graph
        Grafo a visualizar
    title : str
        Título do gráfico
    """
    # Obter graus dos nós
    degrees = count_node_degrees(G)
    node_colors = [degrees[n] for n in G.nodes()]
    
    # Layout do grafo
    pos = nx.spring_layout(G, seed=42)
    
    # Desenhar grafo
    nx.draw_networkx_edges(G, pos,
                          edge_color="gray",
                          alpha=0.3,
                          width=0.5)
    
    nx.draw_networkx_nodes(G, pos,
                          node_size=300,
                          node_color=node_colors,
                          cmap=plt.cm.plasma,
                          alpha=0.8)
    
    # Adicionar labels com o grau de cada nó
    labels = {n: str(degrees[n]) for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels,
                           font_size=8,
                           font_weight='bold',
                           font_color='white')
    
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()