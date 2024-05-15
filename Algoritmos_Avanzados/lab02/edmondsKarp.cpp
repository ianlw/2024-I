/*
    Autor: Callapiña Castilla Ciro Gabriel
           Garcia Romero Jhonatan Alexander
           Colque Galindo Jean Franco
    curso: algorimos avanzados
    Nombre: edmondsKarp.cpp
    Descripcion: Implementacion del flujo maximo mediante Edmonds Karp
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Estructura para representar los arcos del grafo
struct Edge {
    int to, capacity, flow;
};

// Funci�n para agregar una arista dirigida al grafo
void addEdge(vector<vector<Edge>>& graph, int u, int v, int capacity) {
    graph[u].push_back({ v, capacity, 0 });
}

// Funci�n para encontrar un camino de aumento usando BFS
bool bfs(vector<vector<Edge>>& graph, vector<int>& parent, int source, int sink) {
    int n = graph.size();
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(source);
    visited[source] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (Edge& e : graph[u]) {
            int v = e.to;
            if (!visited[v] && e.capacity - e.flow > 0) {
                parent[v] = u;
                visited[v] = true;
                q.push(v);
            }
        }
    }

    return visited[sink];
}

// Implementaci�n del algoritmo de Edmonds-Karp
int edmondsKarp(vector<vector<Edge>>& graph, int source, int sink) {
    int n = graph.size();
    vector<int> parent(n, -1);
    int maxFlow = 0;

    while (bfs(graph, parent, source, sink)) {
        int pathFlow = INT_MAX;
        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            for (Edge& e : graph[u]) {
                if (e.to == v) {
                    pathFlow = min(pathFlow, e.capacity - e.flow);
                    break;
                }
            }
        }

        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            for (Edge& e : graph[u]) {
                if (e.to == v) {
                    e.flow += pathFlow;
                    for (Edge& backEdge : graph[v]) {
                        if (backEdge.to == u) {
                            backEdge.flow -= pathFlow;
                            break;
                        }
                    }
                    break;
                }
            }
        }

        maxFlow += pathFlow;
    }

    return maxFlow;
}

int main() {
    int numNodes = 6; // N�mero de nodos en el grafo
    int source = 0;   // Nodo fuente
    int sink = 5;     // Nodo sumidero

    vector<vector<Edge>> graph(numNodes);

    // Agregar aristas al grafo seg�n el grafo dado
    addEdge(graph, 0, 1, 16);
    addEdge(graph, 0, 2, 13);
    addEdge(graph, 1, 2, 4);
    addEdge(graph, 1, 3, 12);
    addEdge(graph, 2, 1, 10);
    addEdge(graph, 2, 4, 14);
    addEdge(graph, 3, 2, 9);
    addEdge(graph, 3, 5, 20);
    addEdge(graph, 4, 3, 7);
    addEdge(graph, 4, 5, 4);

    int maxFlow = edmondsKarp(graph, source, sink);
    cout << "Flujo m�ximo: " << maxFlow << endl;

    return 0;
}
