import networkx as nx

class UnionFind:
    """Estrutura auxiliar para detectar ciclos na MST."""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal_mst(G):
    """
    Executa o Algoritmo de Kruskal.
    Retorna um novo grafo contendo apenas a Árvore Geradora Mínima e seu custo total.
    """
    mst = nx.Graph()
    mst.add_nodes_from(G.nodes())
    
    # 1. Ordenar todas as arestas em ordem crescente de peso
    edges = [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    edges = sorted(edges, key=lambda item: item[2])
    
    uf = UnionFind(G.nodes())
    
    custo_total = 0
    # 2. Iterar pelas arestas ordenadas e adicionar à MST se não formar ciclo
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.add_edge(u, v, weight=weight)
            custo_total += weight
            
    return mst, custo_total