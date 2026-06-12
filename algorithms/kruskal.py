import networkx as nx


class UnionFind:
    """
    Estrutura auxiliar utilizada pelo algoritmo de Kruskal
    para detectar ciclos.
    """

    def __init__(self, vertices):

        self.parent = {
            v: v
            for v in vertices
        }

        self.rank = {
            v: 0
            for v in vertices
        }

    def find(self, item):

        if self.parent[item] != item:
            self.parent[item] = self.find(
                self.parent[item]
            )

        return self.parent[item]

    def union(self, x, y):

        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return

        if self.rank[raiz_x] < self.rank[raiz_y]:

            self.parent[raiz_x] = raiz_y

        elif self.rank[raiz_x] > self.rank[raiz_y]:

            self.parent[raiz_y] = raiz_x

        else:

            self.parent[raiz_y] = raiz_x
            self.rank[raiz_x] += 1


def kruskal_mst(G):
    """
    Executa o algoritmo de Kruskal.

    Retorna:

        mst
        custo_total
    """

    mst = nx.Graph()

    #
    # IMPORTANTE:
    # copia TODOS os atributos dos nós
    #

    for node, attrs in G.nodes(data=True):

        mst.add_node(
            node,
            **attrs,
        )

    #
    # ordena arestas por peso
    #

    edges = sorted(

        G.edges(data=True),

        key=lambda edge: edge[2]["weight"],

    )

    uf = UnionFind(G.nodes())

    custo_total = 0

    for u, v, attrs in edges:

        if uf.find(u) != uf.find(v):

            uf.union(u, v)

            mst.add_edge(

                u,

                v,

                **attrs,

            )

            custo_total += attrs["weight"]

    return mst, custo_total