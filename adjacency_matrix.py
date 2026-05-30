import networkx as nx
import numpy as np
import pandas as pd
from simple_connected_graphs import generate_simple_connected_graph

def get_adjacency_matrix(G):
    """
    Obtém a matriz de adjacência de um grafo.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo
    
    Returns
    -------
    numpy.ndarray
        Matriz de adjacência
    """
    return nx.to_numpy_array(G, dtype=int)


def get_adjacency_dataframe(G):
    """
    Obtém a matriz de adjacência como DataFrame (pandas) com labels de nós.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo
    
    Returns
    -------
    pandas.DataFrame
        Matriz de adjacência com labels
    """
    adj_matrix = get_adjacency_matrix(G)
    nodes = sorted(G.nodes())
    return pd.DataFrame(adj_matrix, index=nodes, columns=nodes)


def print_adjacency_matrix(G, name=""):
    """
    Exibe a matriz de adjacência de forma legível.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo
    name : str
        Nome do grafo para exibição
    """
    df = get_adjacency_dataframe(G)
    
    print(f"\n{'='*80}")
    print(f"MATRIZ DE ADJACÊNCIA {name}")
    print(f"{'='*80}")
    print(df)
    print(f"{'='*80}\n")


def save_adjacency_matrix_to_csv(G, filename):
    """
    Salva a matriz de adjacência em um arquivo CSV.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo
    filename : str
        Caminho do arquivo CSV
    """
    df = get_adjacency_dataframe(G)
    df.to_csv(filename)
    print(f"Matriz de adjacência salva em: {filename}")


def analyze_adjacency_properties(G):
    """
    Analisa propriedades da matriz de adjacência.
    
    Parameters
    ----------
    G : networkx.Graph
        Grafo
    """
    adj_matrix = get_adjacency_matrix(G)
    
    print(f"\nPROPRIEDADES DA MATRIZ DE ADJACÊNCIA:")
    print(f"Dimensão: {adj_matrix.shape}")
    print(f"Número de 1s (arestas contadas 2x): {np.sum(adj_matrix)}")
    print(f"Número de arestas: {np.sum(adj_matrix) // 2}")
    print(f"É simétrica: {np.allclose(adj_matrix, adj_matrix.T)}")
    print(f"Diagonal (auto-loops): {np.diag(adj_matrix)}")
    print(f"Soma por linha (grau de cada nó):\n{np.sum(adj_matrix, axis=1).astype(int)}")


def generate_and_display_adjacency_matrices():
    """
    Gera grafos simples e conexos e exibe suas matrizes de adjacência.
    """
    sizes = [10, 50, 100]
    
    for n in sizes:
        G = generate_simple_connected_graph(n)
        print(f"\n{'#'*80}")
        print(f"GRAFO COM n={n}")
        print(f"{'#'*80}")
        
        if n <= 10:
            # Exibe a matriz completa para grafos pequenos
            print_adjacency_matrix(G, f"(n={n})")
        else:
            # Para grafos maiores, exibe apenas as dimensões e propriedades
            adj_matrix = get_adjacency_matrix(G)
            print(f"\nDimensão da matriz: {adj_matrix.shape}")
            print(f"Número de arestas: {G.number_of_edges()}")
            analyze_adjacency_properties(G)
        
        # Salvar em CSV
        csv_file = f"adjacency_matrix_n{n}.csv"
        save_adjacency_matrix_to_csv(G, csv_file)


if __name__ == "__main__":
    generate_and_display_adjacency_matrices()
