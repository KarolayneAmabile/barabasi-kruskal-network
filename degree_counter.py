import networkx as nx

def count_node_degrees(G):
    """
    Conta e retorna o grau de cada nó no grafo.
    
    G : networkx.Graph
        Grafo para contar os graus
    
    Returns
    -------
    dict
        Dicionário com nó como chave e grau como valor
    """
    return dict(G.degree())


def print_degree_info(G):
    """
    Imprime informações detalhadas sobre os graus dos nós.
    
    G : networkx.Graph
        Grafo para analisar
    """
    degrees = count_node_degrees(G)
    
    print("=" * 50)
    print("INFORMAÇÕES DE GRAU DOS NÓS")
    print("=" * 50)
    print(f"Número de nós: {G.number_of_nodes()}")
    print(f"Número de arestas: {G.number_of_edges()}")
    print(f"Grau mínimo: {min(degrees.values())}")
    print(f"Grau máximo: {max(degrees.values())}")
    print(f"Grau médio: {sum(degrees.values()) / len(degrees):.2f}")
    print("\nGrau de cada nó:")
    for node, degree in sorted(degrees.items()):
        print(f"  Nó {node}: grau {degree}")
    print("=" * 50)
