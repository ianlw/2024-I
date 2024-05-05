#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

// Definir la función para calcular la FFT
std::vector<std::complex<double>> fft(const std::vector<double>& x) {
    int N = x.size();
    std::vector<std::complex<double>> X(N);

    for (int k = 0; k < N; ++k) {
        for (int n = 0; n < N; ++n) {
            X[k] += x[n] * std::exp(std::complex<double>(0, -2 * M_PI * k * n / N));
        }
    }

    return X;
}

int main() {
    // Ejemplo de entrada: secuencia de números reales
    std::vector<double> x = {1.0, 2.0, 3.0, 4.0};

    // Calcular la FFT de la secuencia
    std::vector<std::complex<double>> X = fft(x);

    // Imprimir los resultados de la FFT
    for (int i = 0; i < X.size(); ++i) {
        std::cout << "X[" << i << "] = " << X[i] << std::endl;
    }

    return 0;
}
