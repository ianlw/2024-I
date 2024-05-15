import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Edge:
    def __init__(self, to, capacity, flow):
        self.to = to
        self.capacity = capacity
        self.flow = flow

def addEdge(graph, u, v, capacity):
    graph[u].append(Edge(v, capacity, 0))

def bfs(graph, parent, source, sink):
    n = len(graph)
    visited = [False] * n
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        for e in graph[u]:
            v = e.to
            if not visited[v] and e.capacity - e.flow > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)

    return visited[sink]

def edmondsKarp(graph, source, sink):
    n = len(graph)
    parent = [-1] * n
    maxFlow = 0

    while bfs(graph, parent, source, sink):
        pathFlow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            for e in graph[u]:
                if e.to == v:
                    pathFlow = min(pathFlow, e.capacity - e.flow)
                    break
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            for e in graph[u]:
                if e.to == v:
                    e.flow += pathFlow
                    for backEdge in graph[v]:
                        if backEdge.to == u:
                            backEdge.flow -= pathFlow
                            break
                    break
            v = parent[v]

        maxFlow += pathFlow

    return maxFlow

def clear_interface():
    for widget in graph_frame.winfo_children():
        widget.destroy()

def calculate_max_flow():
    try:
        numNodes = int(numNodes_entry.get())
        source = int(source_entry.get())
        sink = int(sink_entry.get())

        graph = [[] for _ in range(numNodes)]

        edges_info = edges_entry.get("1.0", tk.END).strip().split("\n")
        for edge_info in edges_info:
            u, v, capacity = map(int, edge_info.split())
            addEdge(graph, u, v, capacity)

        maxFlow = edmondsKarp(graph, source, sink)
        messagebox.showinfo("Resultado", f"Flujo máximo calculado: {maxFlow}")

        global G
        G = nx.DiGraph()
        for i in range(numNodes):
            G.add_node(i)

        for u in range(numNodes):
            for edge in graph[u]:
                G.add_edge(u, edge.to, capacity=edge.capacity, flow=edge.flow)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def show_graph():
    try:
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, arrows=True)

        edge_labels = {(u, v): f"{d['flow']}/{d['capacity']}" for (u, v, d) in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Grafo con Flujo Máximo")
        plt.show()
    except NameError:
        messagebox.showerror("Error", "Primero calcula el flujo máximo")

root = tk.Tk()
root.title("Cálculo de Flujo Máximo")

graph_frame = tk.Frame(root)
graph_frame.pack(padx=10, pady=10)

numNodes_label = tk.Label(graph_frame, text="Número de nodos:")
numNodes_label.grid(row=0, column=0, padx=5, pady=5)
numNodes_entry = tk.Entry(graph_frame)
numNodes_entry.grid(row=0, column=1, padx=5, pady=5)

source_label = tk.Label(graph_frame, text="Nodo fuente:")
source_label.grid(row=1, column=0, padx=5, pady=5)
source_entry = tk.Entry(graph_frame)
source_entry.grid(row=1, column=1, padx=5, pady=5)

sink_label = tk.Label(graph_frame, text="Nodo sumidero:")
sink_label.grid(row=2, column=0, padx=5, pady=5)
sink_entry = tk.Entry(graph_frame)
sink_entry.grid(row=2, column=1, padx=5, pady=5)

edges_label = tk.Label(graph_frame, text="Aristas (u v capacidad):")
edges_label.grid(row=3, column=0, padx=5, pady=5)
edges_entry = tk.Text(graph_frame, height=4, width=20)
edges_entry.grid(row=3, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calcular Flujo Máximo", command=calculate_max_flow)
calculate_button.pack(padx=10, pady=5)

show_graph_button = tk.Button(root, text="Mostrar Grafo", command=show_graph)
show_graph_button.pack(padx=10, pady=5)

root.mainloop()
