#include <chrono>
#include <cmath>
#include <complex>
#include <iostream>
using namespace std ::chrono;
using namespace std;
const double PI = 3.141592653589793238463;
typedef complex<double> Complex;
// Funcion para realizar la Transformada Rapida de Fourier ( FFT)

void FFT(Complex P[], int n)
{
    if (n == 1)
    {
        return;
    }
    Complex w = polar(1.0, -2 * PI / n);
    Complex Pe[n / 2], Po[n / 2];
    // Dividir en partes pares e impares
    for (int i = 0; i < n; i += 2)
    {
        Pe[i / 2] = P[i];
        Po[i / 2] = P[i + 1];
    }
    FFT(Pe, n / 2); // Llamada recursiva a FFT para las partes pares
    FFT(Po, n / 2); // Llamada recursiva a FFT para las partes impares
    Complex t = 1.0;
    for (int j = 0; j < n / 2; j++)
    {
        Complex u = Pe[j];
        P[j] = u + t * Po[j]; // Combinar las partes pares e impares 
        P[j + n / 2] = u - t * Po[j];
        t *= w;
    }
}
// Funcion para realizar la Transformada Inversa Rapida de Fourier(IFFT) 
void IFFT(Complex P[], int n)
{
    if (n == 1)
    {
        return;
    }
    Complex w = polar(1.0, 2 * PI / n);
    Complex Pe[n / 2], Po[n / 2];
    // Dividir en partes pares e impares
    for (int i = 0; i < n; i += 2)
    {
        Pe[i / 2] = P[i];
        Po[i / 2] = P[i + 1];
    }
    IFFT(Pe, n / 2);     // Llamada recursiva a IFFT para las partes pares 
    IFFT(Po, n / 2); // Llamada recursiva a IFFT para las partes impares 
        Complex t = 1.0;
    for (int j = 0; j < n / 2; j++)
    {
        Complex u = Pe[j];
        P[j] = u + t * Po[j]; // Combinar las partes pares e impares 
            P[j + n / 2] = u - t * Po[j];
        t *= w;
    }
}
// Funcion para multiplicar dos polinomios representados como arreglos A y B 
void multiply_polynomials(const int A[], const int B[], int m, int n, int C[])
{
    int k = 1;
    while (k < m + n - 1)
    {
        k *= 2;
    }
    Complex Ac[k], Bc[k];
    // Inicializar los arreglos complejos a partir de los polinomios A y B 
    for (int i = 0; i < m; i++)
    {
        Ac[i] = Complex(A[i]);
    }
    for (int i = 0; i < n; i++)
    {
        Bc[i] = Complex(B[i]);
    }
    FFT(Ac, k); // Aplicar FFT al polinomio A
    FFT(Bc, k); // Aplicar FFT al polinomio B
    for (int i = 0; i < k; i++)
    {
        Ac[i] *= Bc[i]; // Multiplicar los valores complejos en dominio de frecuencia
    }
    IFFT(Ac, k); // Aplicar IFFT al resultado
    for (int i = 0; i < m + n - 1; i++)
    {
        C[i] = int((Ac[i].real() / k) + 0.5); // Redondear y asignar a C
    }
}
int main()
{
    int A[] = {1, 2, 3}; // A ( x ) = 1 + 2 x + 3 x ^2
    int B[] = {4, 5, 6}; // B ( x ) = 4 + 5 x + 6 x ^2
    int m = sizeof(A) / sizeof(A[0]);
    int n = sizeof(B) / sizeof(B[0]);
    int C[m + n - 1];
    auto start = high_resolution_clock::now();            // Registrar el tiempo de inicio 
    multiply_polynomials(A, B, m, n, C); // C ( x ) = A ( x ) ∗ B ( x )
    auto stop = high_resolution_clock::now();             // Registrar el tiempo de finalizacion 
    auto duration = duration_cast<microseconds>(stop - start);
    // Calcular la duracion en microsegundos
    for (int i = 0; i < m + n - 1; i++)
    {
        cout << C[i] << " ";
    }
    cout << endl;
    cout << "\nTiempo de ejecucion del algoritmo: " << duration.count() << " microsegundos " << endl;
    return 0;
}
