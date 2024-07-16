import networkx as nx
import random
import matplotlib.pyplot as plt

class AlgoritmoGeneticoEnrutamiento:
    def __init__(self, grafo, nodo_inicio, nodo_fin, tam_poblacion=100, num_generaciones=50, prob_crossover=0.8, prob_mutacion=0.2):
        self.G = grafo
        self.nodo_inicio = nodo_inicio
        self.nodo_fin = nodo_fin
        self.tam_poblacion = tam_poblacion
        self.num_generaciones = num_generaciones
        self.prob_crossover = prob_crossover
        self.prob_mutacion = prob_mutacion
        
    def evaluar_ruta(self, individuo):
        total_latencia = 0
        for i in range(len(individuo) - 1):
            if self.G.has_edge(individuo[i], individuo[i+1]):
                total_latencia += self.G[individuo[i]][individuo[i+1]]['latencia']
            else:
                return float('inf'),  # Ruta inválida
        if self.G.has_edge(individuo[-1], individuo[0]):
            total_latencia += self.G[individuo[-1]][individuo[0]]['latencia']
        return total_latencia,

    def generar_ruta(self):
        nodos = list(self.G.nodes())
        nodos.remove(self.nodo_inicio)
        nodos.remove(self.nodo_fin)
        ruta = [self.nodo_inicio] + random.sample(nodos, len(nodos) - 2) + [self.nodo_fin]
        return ruta

    def mutar_ruta(self, individuo):
        nodos = list(self.G.nodes())
        nodos.remove(self.nodo_inicio)
        nodos.remove(self.nodo_fin)
        idx1, idx2 = random.sample(range(1, len(individuo) - 1), 2)
        individuo[idx1], individuo[idx2] = random.sample(nodos, 2)
        return individuo

    def crossover(self, ind1, ind2):
        tam = min(len(ind1), len(ind2))
        punto_cx1 = random.randint(1, tam - 1)
        punto_cx2 = random.randint(1, tam - 1)
        if punto_cx1 > punto_cx2:
            punto_cx1, punto_cx2 = punto_cx2, punto_cx1
        ind1[punto_cx1:punto_cx2], ind2[punto_cx1:punto_cx2] = ind2[punto_cx1:punto_cx2], ind1[punto_cx1:punto_cx2]
        return ind1, ind2

    def seleccionar(self, poblacion, k):
        seleccionados = random.sample(poblacion, k)
        seleccionados.sort(key=lambda x: self.evaluar_ruta(x)[0])
        return seleccionados

    def ejecutar(self):
        # Inicializar población
        poblacion = [self.generar_ruta() for _ in range(self.tam_poblacion)]

        # Ejecutar algoritmo genético
        for gen in range(self.num_generaciones):
            descendencia = []
            for _ in range(len(poblacion)):
                ind1, ind2 = random.choices(poblacion, k=2)
                if random.random() < self.prob_crossover:
                    ind1, ind2 = self.crossover(ind1[:], ind2[:])
                if random.random() < self.prob_mutacion:
                    ind1 = self.mutar_ruta(ind1)
                if random.random() < self.prob_mutacion:
                    ind2 = self.mutar_ruta(ind2)
                descendencia.append(ind1)
                descendencia.append(ind2)
            
            poblacion = self.seleccionar(descendencia, k=self.tam_poblacion)

        # Obtener la mejor ruta encontrada
        mejor_individuo = min(poblacion, key=lambda x: self.evaluar_ruta(x)[0])
        mejor_latencia_ruta = self.evaluar_ruta(mejor_individuo)[0]

        return mejor_individuo, mejor_latencia_ruta

    def graficar_mejor_ruta(self, mejor_individuo):
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(10, 6))

        # Dibujar el grafo
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels={(u, v): d['latencia'] for u, v, d in self.G.edges(data=True)})

        # Resaltar la mejor ruta
        mejores_aristas_ruta = [(mejor_individuo[i], mejor_individuo[i+1]) for i in range(len(mejor_individuo) - 1)]
        nx.draw_networkx_edges(self.G, pos, edgelist=mejores_aristas_ruta, edge_color='r', width=2)

        plt.title("Mejor ruta encontrada con algoritmo genético (optimización de enrutamiento)")
        plt.show()

# Crear un grafo de red simulado con NetworkX
G = nx.Graph()
aristas = [
    (0, 1, {'latencia': 5}), (0, 2, {'latencia': 3}), (1, 2, {'latencia': 2}),
    (1, 3, {'latencia': 4}), (2, 3, {'latencia': 1}), (2, 4, {'latencia': 6}),
    (3, 4, {'latencia': 2}), (3, 5, {'latencia': 3}), (4, 5, {'latencia': 4})
]
G.add_edges_from(aristas)

# Crear una instancia del algoritmo genético para enrutamiento
algoritmo_enrutamiento = AlgoritmoGeneticoEnrutamiento(grafo=G, nodo_inicio=0, nodo_fin=5)

# Ejecutar el algoritmo genético para encontrar la mejor ruta de enrutamiento
mejor_individuo, mejor_latencia_ruta = algoritmo_enrutamiento.ejecutar()

print("Mejor ruta encontrada:", mejor_individuo)
print("Latencia de la mejor ruta:", mejor_latencia_ruta)

# Visualizar la mejor ruta de enrutamiento encontrada
algoritmo_enrutamiento.graficar_mejor_ruta(mejor_individuo)
