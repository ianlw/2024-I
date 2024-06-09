#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace std::chrono;

// Función para obtener el dígito en la posición especificada
int obtenerDigito(int numero, int posicion) {
    while (posicion--)
        numero /= 10;
    return numero % 10;
}

// Función de ordenamiento estable por el i-ésimo dígito
void countingSort(vector<int>& A, int n, int posicion) {
    vector<int> conteo(10, 0); // Inicializar conteo de dígitos

    // Contar la ocurrencia de cada dígito
    for (int i = 0; i < n; ++i)
        conteo[obtenerDigito(A[i], posicion)]++;

    // Calcular la posición final de cada elemento
    for (int i = 1; i < 10; ++i)
        conteo[i] += conteo[i - 1];

    vector<int> resultado(n); // Vector para almacenar el resultado ordenado

    // Construir el vector ordenado
    for (int i = n - 1; i >= 0; --i) {
        resultado[conteo[obtenerDigito(A[i], posicion)] - 1] = A[i];
        conteo[obtenerDigito(A[i], posicion)]--;
    }

    // Copiar el resultado ordenado de vuelta al vector original
    for (int i = 0; i < n; ++i)
        A[i] = resultado[i];
}

// Función principal para realizar el Radix Sort
void radixSort(vector<int>& A, int n, int d) {
    // Aplicar counting sort para cada dígito, desde el menos significativo al más significativo
    for (int i = 0; i < d; ++i)
        countingSort(A, n, i);
}

void tiempo_radixsort(int tamano) {
    vector<int> A(tamano);

    // Llenar el vector con números aleatorios
    for (int i = 0; i < tamano; ++i) {
        A[i] = rand() % 10000; // Números aleatorios entre 0 y 9999
    }

    auto inicio = high_resolution_clock::now();
    radixSort(A, tamano, 4); // Se supone que los números tienen hasta 4 dígitos
    auto fin = high_resolution_clock::now();

    duration<double> duracion = fin - inicio;

    cout << fixed << setprecision(10) << "Tiempo para " << tamano << " elementos: " << duracion.count() << " segundos." << endl;
}

int main() {
    // Semilla para la generación de números aleatorios
    srand(time(nullptr));

    // Ejecutar Radix Sort con diferentes tamaños de vector
    tiempo_radixsort(10);
    tiempo_radixsort(100);
    tiempo_radixsort(1000);
    tiempo_radixsort(10000);
    tiempo_radixsort(100000);

    return 0;
}
