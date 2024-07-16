from tabulate import tabulate

def minimum_multiplications_dp(b):
    n = len(b) - 1  # número de matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]  # tabla para almacenar el número mínimo de multiplicaciones
    s = [[0] * (n + 1) for _ in range(n + 1)]  # tabla para almacenar los puntos de división óptimos

    # Recorremos todas las subcadenas de tamaño creciente
    for u in range(1, n):  # tamaño de la subcadena
        for i in range(1, n - u + 1):
            j = i + u
            m[i][j] = float('inf')  # Inicializamos el número mínimo de multiplicaciones como infinito
            # Buscamos el mejor punto de división para la subcadena (i, j)
            for k in range(i, j):
                # Calculamos el número de multiplicaciones para dividir en k
                q = m[i][k] + m[k + 1][j] + b[i - 1] * b[k] * b[j]
                # Si encontramos una menor cantidad de multiplicaciones, actualizamos m[i][j] y s[i][j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

# Ejemplo de uso
matrices_dimensiones = [200, 2, 30, 20, 5]  # las dimensiones de las matrices b0, b1, ..., bn
m, s = minimum_multiplications_dp(matrices_dimensiones)

# Imprimir la tabla m usando tabulate
headers = [""] + [f"j={j}" for j in range(1, len(m))]
table_m = [[f"i={i}"] + row[1:] for i, row in enumerate(m[1:], start=1)]
print("Tabla m:")
waw="html"
print(tabulate(table_m, headers=headers, tablefmt=waw))

print("\nTabla s:")
table_s = [[f"i={i}"] + row[1:] for i, row in enumerate(s[1:], start=1)]
print(tabulate(table_s, headers=headers, tablefmt=waw))
