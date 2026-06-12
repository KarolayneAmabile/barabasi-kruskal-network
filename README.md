# Projeto de Teoria dos Grafos: Barabási-Albert e Kruskal

Este projeto gera grafos aleatórios utilizando o modelo de **Barabási-Albert** com pesos nas arestas (1 a 20). Em seguida, aplica o algoritmo de **Kruskal** para encontrar a Árvore Geradora Mínima (MST), exportando matrizes de adjacência e de custo, além de exibir as interfaces gráficas.

O programa processa sequencialmente grafos de tamanhos **n = 10**, **n = 50** e **n = 100**.

## 📂 Estrutura do Projeto

```text
projeto_grafos/
├── main.py                  # Script principal para rodar o projeto
├── models/
│   └── gerador_grafos.py    # Algoritmo Barabási-Albert do zero com pesos
├── algorithms/
│   └── kruskal.py           # Algoritmo de Kruskal (com Union-Find) do zero
├── utils/
│   └── visualizer.py        # Interface gráfica (Matplotlib)
├── requirements.txt         # Dependências do projeto
└── README.md                # Instruções de execução