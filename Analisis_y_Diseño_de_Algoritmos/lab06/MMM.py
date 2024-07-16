def memoization(m, s, b, i, j):
    if m[i][j] < float('inf'):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = memoization(m, s, b, i, k) + memoization(m, s, b, k + 1, j) + b[i - 1] * b[k] * b[j]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return m[i][j]

def minimum_multiplications_memoized(b):
    n = len(b) - 1  # número de matrices
    m = [[float('inf')] * (n + 1) for _ in range(n + 1)]  # matriz de memorización para almacenar resultados
    s = [[0] * (n + 1) for _ in range(n + 1)]  # matriz para almacenar puntos de división óptimos

    memoization(m, s, b, 1, n)
    return m[1][n], s  # retornar también la matriz s con los puntos de división óptimos

def minimum_multiplications(b):
    min_multiplicaciones, puntos_division_optimos = minimum_multiplications_memoized(b)
    return min_multiplicaciones

# Ejemplo de uso
matrices_dimensiones = [10, 30, 5, 60, 80]  # las dimensiones de las matrices b0, b1, ..., bn
min_multiplicaciones = minimum_multiplications(matrices_dimensiones)
print(f"Número mínimo de multiplicaciones necesarias: {min_multiplicaciones}")

