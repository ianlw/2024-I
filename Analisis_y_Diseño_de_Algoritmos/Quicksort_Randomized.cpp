#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono> // Para medir el tiempo de ejecución
#include <iomanip>

using namespace std;
using namespace std::chrono;

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int obtenerIndiceAleatorio(int p, int r) {
    return p + rand() % (r - p + 1);
}

int particionAleatoria(vector<int>& A, int p, int r) {
    int i = obtenerIndiceAleatorio(p, r);
    swap(A[i], A[r]);
    int pivot = A[r];
    i = p - 1;
    for (int j = p; j < r; ++j) {
        if (A[j] <= pivot) {
            i++;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[r]);
    return i + 1;
}

void quickSortAleatorio(vector<int>& A, int p, int r) {
    if (p < r) {
        int q = particionAleatoria(A, p, r);
        quickSortAleatorio(A, p, q - 1);
        quickSortAleatorio(A, q + 1, r);
    }
}

void tiempo_quicksort_randomized(int tamano) {
    vector<int> A(tamano);

    // Llenar el vector con números aleatorios
    for (int i = 0; i < tamano; ++i) {
        A[i] = rand() % 10000; // Números aleatorios entre 0 y 9999
    }

    auto inicio = high_resolution_clock::now();
    quickSortAleatorio(A, 0, tamano - 1);
    auto fin = high_resolution_clock::now();

    duration<double> duracion = fin - inicio;

    cout << fixed << setprecision(10) << "Tiempo para " << tamano << " elementos: " << duracion.count() << " segundos" << endl;
}

int main() {
    // Semilla para la generación de números aleatorios
    srand(time(nullptr));

    // Ejecutar QuickSort Aleatorio con diferentes tamaños de vector
    tiempo_quicksort_randomized(10);
    tiempo_quicksort_randomized(100);
    tiempo_quicksort_randomized(1000);
    tiempo_quicksort_randomized(10000);
    tiempo_quicksort_randomized(100000);

    return 0;
}
