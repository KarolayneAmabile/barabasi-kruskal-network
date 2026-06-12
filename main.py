import os
from models.gerador_grafos import barabasi_albert_com_custo, extrair_matrizes
from algorithms.kruskal import kruskal_mst
from utils.visualizer import plotar_grafo_e_mst

def main():
    # Prepara o diretório para salvar as matrizes e imagens
    pasta_saida = "outputs"
    os.makedirs(pasta_saida, exist_ok=True)
    
    tamanhos = [10, 50, 100]
    m = 2  # Arestas por novo nó no modelo Barabási-Albert
    
    for n in tamanhos:
        print(f"\n{'='*60}")
        print(f"PROCESSANDO GRAFO n = {n}")
        print(f"{'='*60}")
        
        # --- ITENS 1 e 3 ---
        G = barabasi_albert_com_custo(n, m, seed=42)
        print(f"Grafo gerado: {G.number_of_nodes()} nós, {G.number_of_edges()} arestas.")
        
        # --- ITEM 2 ---
        df_adj, df_cost = extrair_matrizes(G)
        
        # Salva em CSV no computador
        df_adj.to_csv(f"{pasta_saida}/matriz_adjacencia_n{n}.csv")
        df_cost.to_csv(f"{pasta_saida}/matriz_custo_n{n}.csv")
        print(f"Matrizes (Adjacência e Custo) exportadas para '{pasta_saida}/'.")
        
        if n == 10:
            print("\nMatriz de Adjacência gerada para n=10 (Exibição no terminal):")
            print(df_adj)
            print("\nMatriz de Custo gerada para n=10 (Exibição no terminal):")
            print(df_cost)
        
        # --- ITEM 5 e 6 ---
        mst, custo_total = kruskal_mst(G)
        print(f"\nKruskal Executado. Árvore Geradora Mínima (MST) criada!")
        print(f"Número de arestas na MST: {mst.number_of_edges()}")
        print(f"Custo mínimo total para conectar todos os nós: {custo_total}")
        
        # --- ITEM 7 ---
        print("\nAbrindo Interface Gráfica (Feche a janela para continuar para o próximo tamanho de grafo)...")
        plotar_grafo_e_mst(G, mst, n, pasta_saida)

if __name__ == "__main__":
    main()