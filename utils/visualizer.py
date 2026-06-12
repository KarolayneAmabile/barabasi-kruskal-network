import matplotlib.pyplot as plt
import networkx as nx


def plotar_grafo_e_mst(G, mst, n, pasta_saida="outputs"):
    """
    Desenha lado a lado:

    - Grafo original
    - Árvore Geradora Mínima (Kruskal)

    Para grafos geográficos (latitude/longitude):
        - utiliza as coordenadas reais;
        - mostra o nome dos estabelecimentos.

    Para grafos Barabási-Albert:
        - utiliza spring_layout;
        - mostra o grau dos nós.
    """

    fig, axes = plt.subplots(1, 2, figsize=(18, 9))

    possui_coordenadas = all(
        "latitude" in G.nodes[node]
        and "longitude" in G.nodes[node]
        for node in G.nodes
    )

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------

    if possui_coordenadas:

        pos = {
            node: (
                G.nodes[node]["longitude"],
                G.nodes[node]["latitude"],
            )
            for node in G.nodes
        }

        titulo = "Locais de Anápolis"

    else:

        pos = nx.spring_layout(G, seed=42)

        titulo = f"Barabási-Albert (n={n})"

    # ==================================================
    # GRAFO ORIGINAL
    # ==================================================

    axes[0].set_title(
        f"Grafo Original ({titulo})",
        fontsize=12,
    )

    nx.draw_networkx_edges(
        G,
        pos,
        ax=axes[0],
        edge_color="gray",
        alpha=0.4,
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        ax=axes[0],
        node_size=350,
        node_color="lightblue",
    )

    if possui_coordenadas:

        labels = {
            node: node
            for node in G.nodes()
        }

    else:

        labels = {
            node: str(grau)
            for node, grau in G.degree()
        }

    nx.draw_networkx_labels(
        G,
        pos,
        labels=labels,
        ax=axes[0],
        font_size=7,
    )

    axes[0].axis("off")

    # ==================================================
    # MST
    # ==================================================

    axes[1].set_title(
        "Árvore Geradora Mínima (Kruskal)",
        fontsize=12,
    )

    nx.draw_networkx_edges(
        mst,
        pos,
        ax=axes[1],
        edge_color="red",
        width=2,
    )

    nx.draw_networkx_nodes(
        mst,
        pos,
        ax=axes[1],
        node_size=350,
        node_color="lightgreen",
    )

    if possui_coordenadas:

        labels = {
            node: node
            for node in mst.nodes()
        }

    else:

        labels = {
            node: str(grau)
            for node, grau in mst.degree()
        }

    nx.draw_networkx_labels(
        mst,
        pos,
        labels=labels,
        ax=axes[1],
        font_size=7,
    )

    axes[1].axis("off")

    plt.tight_layout()

    caminho = f"{pasta_saida}/interface_grafos_n{n}.png"

    plt.savefig(
        caminho,
        dpi=200,
        bbox_inches="tight",
    )

    print(f"Interface salva em: {caminho}")

    plt.show()

    plt.close(fig)