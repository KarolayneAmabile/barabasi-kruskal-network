import os
import networkx as nx

from models.gerador_grafo_anapolis import (
    construir_grafo,
    extrair_matrizes
)

from algorithms.kruskal import kruskal_mst
from utils.visualizer import plotar_grafo_e_mst


def main():

    pasta_saida = "outputs/anapolis"

    os.makedirs(
        pasta_saida,
        exist_ok=True
    )

    G = construir_grafo(
        "data/locais_anapolis.csv"
    )

    print(
        f"Grafo criado: {G.number_of_nodes()} nós, "
        f"{G.number_of_edges()} arestas"
    )

    nx.write_graphml(
        G,
        f"{pasta_saida}/grafo.graphml"
    )

    adj, custo = extrair_matrizes(G)

    adj.to_csv(
        f"{pasta_saida}/matriz_adjacencia.csv"
    )

    custo.to_csv(
        f"{pasta_saida}/matriz_custo.csv"
    )

    mst, custo_total = kruskal_mst(G)

    print()
    print("Resultado do Kruskal")
    print("--------------------")
    print(f"Custo total: {custo_total}")

    plotar_grafo_e_mst(
        G,
        mst,
        "anapolis",
        pasta_saida
    )


if __name__ == "__main__":
    main()