import pandas as pd


def exportar_arestas_mst(mst, caminho_saida):
    """
    Exporta as arestas da MST para um arquivo CSV.

    Colunas:
        - origem
        - destino
        - distancia_metros
    """

    linhas = []

    for origem, destino, dados in mst.edges(data=True):

        linhas.append({
            "origem": origem,
            "destino": destino,
            "distancia_metros": round(
                dados.get("weight", 0),
                2,
            ),
        })

    df = pd.DataFrame(linhas)

    df = df.sort_values(
        by="distancia_metros"
    )

    df.to_csv(
        caminho_saida,
        index=False,
    )

    print(
        f"Arestas da MST exportadas para: "
        f"{caminho_saida}"
    )