def toom_cook_multiply(a, b):
    # Convierte los números en listas de dígitos
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]

    # Divide las listas en partes más pequeñas en 3 partes (Toom-3)
    n = max(len(a_digits), len(b_digits))
    split_size = n // 3

    a_parts = [a_digits[i:i + split_size] for i in range(0, len(a_digits), split_size)]
    b_parts = [b_digits[i:i + split_size] for i in range(0, len(b_digits), split_size)]

    # Realiza la multiplicación de las partes
    result_parts = []
    for i in range(len(a_parts)):
        part_result = 0
        for j in range(len(b_parts)):
            part_result += int(''.join(map(str, a_parts[i]))) * int(''.join(map(str, b_parts[j])))
        result_parts.append(part_result)

    # Combina los resultados de las partes
    result = 0
    for i, part in enumerate(result_parts):
        result += part * 10**(split_size * i)

    return result

# Ejemplo de uso:
a = 123456789
b = 987654321
print("Numero 1:", a)
print("Numero 2:", b)
resultado = toom_cook_multiply(a, b)
print("Resultado de la multiplicación usando el algoritmo de Toom-Cook:\n",resultado)
