import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox


def plotar_mst_no_mapa(
    road,
    mst,
    caminho_saida,
):

    fig, ax = ox.plot_graph(
        road,
        show=False,
        close=False,
        node_size=0,
        edge_linewidth=0.5,
        edge_color="lightgray",
        bgcolor="white",
    )
    pos = {}
    for node, attrs in mst.nodes(data=True):
        pos[node] = (
            attrs["x"],
            attrs["y"],
        )

    nx.draw_networkx_edges(
        mst,
        pos,
        ax=ax,
        edge_color="red",
        width=3,
    )

    nx.draw_networkx_nodes(
        mst,
        pos,
        ax=ax,
        node_color="blue",
        node_size=60,
    )

    nx.draw_networkx_labels(
        mst,
        pos,
        ax=ax,
        font_size=7,
    )

    plt.savefig(
        caminho_saida,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)

    print(
        f"Mapa salvo em {caminho_saida}"
    )