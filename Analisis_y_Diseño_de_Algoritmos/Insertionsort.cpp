#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <ctime>

using namespace std;
using namespace std::chrono;

void insertionsort(vector<int>& A) {
    int n = A.size();
    for (int j = 1; j < n; j++) {
        int clave = A[j];
        int i = j - 1;
        while (i >= 0 && A[i] > clave) {
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = clave;
    }
}

void tiempo_insertionsort(int tamano) {
    vector<int> A(tamano);

    // Llenar el vector con números aleatorios
    for (int i = 0; i < tamano; ++i) {
        A[i] = rand() % 10000; // Números aleatorios entre 0 y 9999
    }

    auto inicio = high_resolution_clock::now();
    insertionsort(A);
    auto fin = high_resolution_clock::now();

    duration<double> duracion = fin - inicio;

    cout << fixed << setprecision(10) << "Tiempo para " << tamano << " elementos: " << duracion.count() << " segundos" << endl;
}

int main() {
    // Semilla para la generación de números aleatorios
    srand(time(nullptr));

    // Ejecutar Ordenamiento por Inserción con diferentes tamaños de vector
    tiempo_insertionsort(10);
    tiempo_insertionsort(100);
    tiempo_insertionsort(1000);
    tiempo_insertionsort(10000);
    tiempo_insertionsort(100000);

    return 0;
}
