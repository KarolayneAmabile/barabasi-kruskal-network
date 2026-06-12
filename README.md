# Projeto de Teoria dos Grafos: Modelo Barabási-Albert e Algoritmo de Kruskal

Este projeto implementa conceitos fundamentais de **Teoria dos Grafos** utilizando Python, com foco na geração de grafos pelo modelo **Barabási-Albert** e na aplicação do algoritmo de **Kruskal** para obtenção da **Árvore Geradora Mínima (Minimum Spanning Tree - MST)**.

Além do experimento com grafos sintéticos, o projeto também inclui uma implementação baseada em **dados geográficos reais**, construindo um grafo completo entre estabelecimentos localizados na cidade de **Anápolis (GO)**, utilizando distâncias calculadas sobre a malha viária do **OpenStreetMap**.

## Funcionalidades

### Grafos Barabási-Albert

* Geração de grafos utilizando o modelo Barabási-Albert.
* Atribuição de pesos aleatórios às arestas.
* Execução do algoritmo de Kruskal.
* Exportação da matriz de adjacência.
* Exportação da matriz de custos.
* Visualização gráfica do grafo original e da Árvore Geradora Mínima.

Os experimentos são executados para grafos de tamanhos:

* `n = 10`
* `n = 50`
* `n = 100`

---

### Grafo geográfico de Anápolis

* Construção de um grafo completo a partir de estabelecimentos reais.
* Cálculo do peso das arestas utilizando a menor distância pela malha viária do OpenStreetMap.
* Execução do algoritmo de Kruskal.
* Exportação das matrizes de adjacência e custos.
* Exportação das arestas pertencentes à MST.
* Geração de visualizações do grafo e da árvore geradora mínima.

---

# Estrutura do projeto

```text
barabasi-kruskal-network/
│
├── algorithms/
│   └── kruskal.py
│
├── data/
│   └── locais_anapolis.csv
│
├── models/
│   ├── gerador_grafos.py
│   └── gerador_grafo_anapolis.py
│
├── outputs/
│   └── ...
│
├── utils/
│   ├── exportador.py
│   ├── mapa.py
│   └── visualizer.py
│
├── main.py
├── main_anapolis.py
├── requirements.txt
└── README.md
```

---

# Requisitos

* Python 3.11 ou superior
* pip

---

# Criando o ambiente virtual

## Linux

```bash
python3 -m venv venv
```

Ative o ambiente:

```bash
source venv/bin/activate
```

---

## Windows (PowerShell)

```powershell
python -m venv venv
```

Ative o ambiente:

```powershell
venv\Scripts\Activate.ps1
```

---

# Instalando as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

Caso utilize a versão geográfica do projeto, certifique-se de que o arquivo `requirements.txt` contenha também:

```text
networkx
pandas
matplotlib
osmnx
pyproj
scikit-learn
```

---

# Executando o projeto

## Experimentos com Barabási-Albert

```bash
python main.py
```

Serão gerados:

* matrizes de adjacência;
* matrizes de custo;
* imagens contendo o grafo original e sua MST.

Todos os arquivos serão armazenados na pasta `outputs/`.

---

## Experimento utilizando os locais de Anápolis

```bash
python main_anapolis.py
```

Na primeira execução será realizada automaticamente a obtenção da malha viária da cidade através do OpenStreetMap.

Nas próximas execuções a malha será reutilizada a partir do cache salvo em:

```text
outputs/anapolis/road.graphml
```

---

# Arquivos gerados

Após executar `main_anapolis.py`, serão produzidos arquivos semelhantes a:

```text
outputs/anapolis/

├── arestas_mst.csv
├── grafo.graphml
├── interface_grafos_nanapolis.png
├── matriz_adjacencia.csv
├── matriz_custo.csv
├── mst_mapa_real.png
└── road.graphml
```

Descrição:

* **grafo.graphml**: representação completa do grafo em formato GraphML;
* **matriz_adjacencia.csv**: matriz de adjacência do grafo;
* **matriz_custo.csv**: matriz contendo os pesos (distâncias em metros);
* **arestas_mst.csv**: lista das arestas selecionadas pelo algoritmo de Kruskal;
* **interface_grafos_nanapolis.png**: comparação entre o grafo completo e sua árvore geradora mínima;
* **mst_mapa_real.png**: visualização da MST utilizando as posições geográficas dos estabelecimentos;
* **road.graphml**: cache da malha viária utilizada para cálculo das distâncias.

---

# Dependências principais

* NetworkX
* Matplotlib
* Pandas
* OSMnx
* PyProj
* Scikit-learn

---