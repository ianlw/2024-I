def minimas_multiplicaciones_recursivo(b, i, j, m, s):
    if i == j:
        return 0
    
    if m[i][j] < float('inf'):
        return m[i][j]
    
    for k in range(i, j):
        q = (minimas_multiplicaciones_recursivo(b, i, k, m, s) +
             minimas_multiplicaciones_recursivo(b, k + 1, j, m, s) +
             b[i - 1] * b[k] * b[j])
        
        if m[i][j] > q:
            m[i][j] = q
            s[i][j] = k
    
    return m[i][j]

def calcular_minimas_multiplicaciones(b):
    n = len(b) - 1  # número de matrices
    m = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    return minimas_multiplicaciones_recursivo(b, 1, n, m, s)

# Ejemplo de uso:
vector_b = [30, 35, 15, 5, 10, 20, 25]
min_multiplicaciones = calcular_minimas_multiplicaciones(vector_b)
print("El número mínimo de multiplicaciones escalares es:", min_multiplicaciones)
