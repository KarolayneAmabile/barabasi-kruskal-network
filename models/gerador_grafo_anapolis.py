import pandas as pd
import os
import networkx as nx
import osmnx as ox

from itertools import combinations
from pyproj import Transformer

def construir_grafo(csv_path: str):

    cache = "outputs/anapolis/road.graphml"
    locais = pd.read_csv(csv_path)

    if os.path.exists(cache):
        print("Carregando malha viária salva...")
        road = ox.load_graphml(cache)
    else:
        print("Baixando malha viária de Anápolis...")
        road = ox.graph_from_place(
            "Anápolis, Goiás, Brazil",
            network_type="drive"
        )
        road = ox.project_graph(road)
        os.makedirs(
            "outputs/anapolis",
            exist_ok=True
        )
        ox.save_graphml(
            road,
            cache
        )

    transformer = Transformer.from_crs(
        "EPSG:4326",
        road.graph["crs"],
        always_xy=True,
    )
    
    G = nx.Graph()

    for _, row in locais.iterrows():
        x, y = transformer.transform(
            row["longitude"],
            row["latitude"],
        )

        G.add_node(
            row["nome"],
            latitude=row["latitude"],
            longitude=row["longitude"],
            x=x,
            y=y,
        )

    for i, j in combinations(range(len(locais)), 2):
        origem = locais.iloc[i]
        destino = locais.iloc[j]

        x1, y1 = transformer.transform(
            origem["longitude"],
            origem["latitude"],
        )

        x2, y2 = transformer.transform(
            destino["longitude"],
            destino["latitude"],
        )

        no_origem = ox.distance.nearest_nodes(
            road,
            x1,
            y1,
        )

        no_destino = ox.distance.nearest_nodes(
            road,
            x2,
            y2,
        )

        try:
            distancia = nx.shortest_path_length(
                road,
                no_origem,
                no_destino,
                weight="length"
            )
        except nx.NetworkXNoPath:
            print(
                f"Sem caminho entre "
                f"{origem['nome']} e {destino['nome']}"
            )
            continue

        G.add_edge(
            origem["nome"],
            destino["nome"],
            weight=distancia
        )

    return G, road

def extrair_matrizes(G):

    nos = list(G.nodes())

    matriz_adj = nx.to_pandas_adjacency(
        G,
        nodelist=nos,
        weight=None,
        dtype=int
    )

    matriz_custo = pd.DataFrame(
        0.0,
        index=nos,
        columns=nos
    )

    for u, v, data in G.edges(data=True):

        matriz_custo.loc[u, v] = data["weight"]
        matriz_custo.loc[v, u] = data["weight"]

    return matriz_adj, matriz_custo