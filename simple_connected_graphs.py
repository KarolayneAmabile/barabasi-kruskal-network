import networkx as nx
import matplotlib.pyplot as plt

def generate_simple_connected_graph(n):
    """
    Gera um grafo simples e conexo com n nós.
    
    Usa o modelo Erdős–Rényi com probabilidade ajustada para garantir conexidade.
    
    Parameters
    ----------
    n : int
        Número de nós
    
    Returns
    -------
    networkx.Graph
        Grafo simples e conexo
    """
    # Probabilidade mínima para garantir conexidade
    # Fórmula: p >= log(n) / n
    p = max(2 * (n ** -0.5), 0.1)
    
    G = nx.erdos_renyi_graph(n, p, seed=42)
    
    # Garante que o grafo está conexo
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n, p, seed=42)
        p += 0.05
    
    return G


def print_graph_info(G, name=""):
    """
    Exibe informações sobre o grafo.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo a analisar
    name : str
        Nome do grafo para exibição
    """
    print(f"\n{'='*60}")
    print(f"GRAFO {name}")
    print(f"{'='*60}")
    print(f"Número de nós: {G.number_of_nodes()}")
    print(f"Número de arestas: {G.number_of_edges()}")
    print(f"Densidade: {nx.density(G):.4f}")
    print(f"Está conexo: {nx.is_connected(G)}")
    print(f"Número de componentes: {nx.number_connected_components(G)}")
    print(f"Diâmetro: {nx.diameter(G)}")
    degrees = [G.degree(n) for n in G.nodes()]
    print(f"Grau médio: {sum(degrees) / len(degrees):.2f}")
    print(f"Grau mínimo: {min(degrees)}")
    print(f"Grau máximo: {max(degrees)}")
    print(f"{'='*60}")


def visualize_simple_connected_graphs():
    """
    Gera e visualiza grafos simples e conexos com n=10, n=50, n=100
    """
    sizes = [10, 50, 100]
    graphs = {}
    
    for n in sizes:
        graphs[n] = generate_simple_connected_graph(n)
        print_graph_info(graphs[n], f"(n={n})")
    
    # Visualizar os grafos
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, n in enumerate(sizes):
        G = graphs[n]
        pos = nx.spring_layout(G, seed=42, k=0.5)
        
        ax = axes[idx]
        nx.draw_networkx_nodes(G, pos, node_size=30, ax=ax, alpha=0.7)
        nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.5, ax=ax)
        
        ax.set_title(f"Grafo Simples e Conexo (n={n})")
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return graphs


if __name__ == "__main__":
    graphs = visualize_simple_connected_graphs()
