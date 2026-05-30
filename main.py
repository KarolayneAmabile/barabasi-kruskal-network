from barabasi_krustal import barabasi_albert, visualize_barabasi
from degree_counter import print_degree_info

# Gerar grafo Barabási-Albert
G = barabasi_albert(n=100, m=2, seed=42)

# Exibir informações de grau
print_degree_info(G)

# Visualizar o grafo com labels de grau
visualize_barabasi(G, title="Barabási-Albert — Implementação do zero (n=100, m=2)")
