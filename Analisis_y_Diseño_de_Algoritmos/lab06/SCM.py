def SCM(X, n):
    if n == 1:
        if X[0] < 0:
            return (0, 0, 0, 0, 0)
        else:
            return (1, 1, 2, X[0], X[0])
    
    (i, j, k, MaxSeq, MaxSuf) = SCM(X, n - 1)
    MaxSuf += X[n - 1]
    
    if MaxSuf < 0:
        MaxSuf = 0
        k = n + 1
    
    if MaxSuf > MaxSeq:
        i = k
        j = n
        MaxSeq = MaxSuf
    
    return (i, j, k, MaxSeq, MaxSuf)

# Ejemplos de uso
X1 = [4, 2, -7, 3, 0, -2, 1, 5, -2]
X2 = [-1, -2, 0]
X3 = [-3, -1]

print("Ejemplo 1:")
(i1, j1, _, _, _) = SCM(X1, len(X1))
print(f"Subsecuencia máxima: {X1[i1-1:j1]}")

print("\nEjemplo 2:")
(i2, j2, _, _, _) = SCM(X2, len(X2))
if i2 == 0 and j2 == 0:
    print("No hay subsecuencia máxima.")
else:
    print(f"Subsecuencia máxima: {X2[i2-1:j2]}")

print("\nEjemplo 3:")
(i3, j3, _, _, _) = SCM(X3, len(X3))
if i3 == 0 and j3 == 0:
    print("No hay subsecuencia máxima.")
else:
    print(f"Subsecuencia máxima: {X3[i3-1:j3]}")
