import matplotlib.pyplot as plt
import networkx as nx

def plotar_grafo_e_mst(G, mst, n, pasta_saida="outputs"):
    """
    Gera as interfaces mostrando a representação geométrica do grafo
    e da árvore geradora mínima, com o grau de cada nó dentro do círculo.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Se o grafo possuir coordenadas geográficas, utiliza-as.
    # Caso contrário, utiliza spring_layout.
    if all(
        "latitude" in G.nodes[n] and "longitude" in G.nodes[n]
        for n in G.nodes
    ):

        pos = {
            n: (
                G.nodes[n]["longitude"],
                G.nodes[n]["latitude"],
            )
            for n in G.nodes
        }

    else:

        pos = nx.spring_layout(G, seed=42)
    
    # --- 7.1 Grafo Original ---
    axes[0].set_title(f"Grafo Original (Barabási-Albert n={n})\nOs números nos nós indicam o GRAU", fontsize=12)
    
    # Desenha as arestas
    nx.draw_networkx_edges(G, pos, ax=axes[0], edge_color='gray', alpha=0.4)
    # Desenha os nós (tamanho ligeiramente maior para caber o número)
    nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=250, node_color='lightblue')
    
    # Calcula e desenha os graus do Grafo Original dentro dos nós
    graus_orig = dict(G.degree())
    labels_orig = {no: str(grau) for no, grau in graus_orig.items()}
    nx.draw_networkx_labels(G, pos, labels=labels_orig, ax=axes[0], font_size=8, font_weight='bold')
    
    axes[0].axis('off')
    
    # --- 7.2 Árvore Geradora Mínima ---
    axes[1].set_title("Árvore Geradora Mínima (Kruskal)\nOs números nos nós indicam o GRAU NA ÁRVORE", fontsize=12)
    
    # Desenha as arestas da árvore
    nx.draw_networkx_edges(mst, pos, ax=axes[1], edge_color='red', width=2)
    # Desenha os nós
    nx.draw_networkx_nodes(mst, pos, ax=axes[1], node_size=250, node_color='lightgreen')
    
    # Calcula e desenha os graus da Árvore dentro dos nós
    # (Note que o grau na árvore é diferente do grau no grafo original)
    graus_mst = dict(mst.degree())
    labels_mst = {no: str(grau) for no, grau in graus_mst.items()}
    nx.draw_networkx_labels(mst, pos, labels=labels_mst, ax=axes[1], font_size=8, font_weight='bold')
    
    axes[1].axis('off')
    
    plt.tight_layout()
    caminho_arquivo = f"{pasta_saida}/interface_grafos_n{n}.png"
    plt.savefig(caminho_arquivo, dpi=150)
    print(f"Interface gráfica salva em: {caminho_arquivo}")
    
    # Exibe a interface
    plt.show()