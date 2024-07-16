import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()

# Añadir nodos
G.add_nodes_from([0, 1, 2, 3, 4, 5])

# Añadir bordes con atributo de peso ('latency')
edges = [
    (0, 1, {'latency': 5}),
    (0, 2, {'latency': 3}),
    (1, 2, {'latency': 2}),
    (1, 3, {'latency': 4}),
    (2, 3, {'latency': 1}),
    (2, 4, {'latency': 6}),
    (3, 4, {'latency': 2}),
    (3, 5, {'latency': 3}),
    (4, 5, {'latency': 4})
]
G.add_edges_from(edges)

# Encontrar el MST usando el algoritmo de Prim
MST = nx.minimum_spanning_tree(G, algorithm='prim')

# Visualizar el grafo original y el MST
plt.figure(figsize=(10, 8))

# Posiciones de los nodos para la visualización
pos = nx.spring_layout(G)

# Dibujar el grafo original
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray', font_size=16, font_weight='bold')

# Dibujar el MST encima del grafo original
nx.draw_networkx_edges(MST, pos, edge_color='red', width=2.0)

# Etiquetar los pesos de los bordes del MST
labels = nx.get_edge_attributes(MST, 'latency')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels, font_color='red')

# Mostrar el grafo
plt.title('Grafo original con MST (en rojo)')
plt.show()
