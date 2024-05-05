def obtener_datos_ingresados():
    total_personas = 0
    total_hombres = 0
    total_mujeres = 0
    suma_edades_hombres = 0
    suma_edades_mujeres = 0
    edad_minima = 1000

    while True:
        edad = int(input("Ingrese la edad (0 para terminar): "))
        if edad == 0:
            break
        if edad < 18:
            print("Lo siento, no se permiten menores de edad a la fiesta.")
            continue

        sexo = input("Ingrese el sexo (H/M): ").upper()
        if sexo not in ("H", "M"):
            print("Sexo no válido. Ingrese H para hombre o M para mujer.")
            continue

        total_personas += 1

        if sexo == "H":
            total_hombres += 1
            suma_edades_hombres += edad
        else:
            total_mujeres += 1
            suma_edades_mujeres += edad

        if edad < edad_minima:
            edad_minima = edad

    return total_personas, total_hombres, total_mujeres, suma_edades_hombres, suma_edades_mujeres, edad_minima

def calcular_promedios(total_hombres, total_mujeres, suma_edades_hombres, suma_edades_mujeres):
    promedio_edades_hombres = suma_edades_hombres / total_hombres if total_hombres > 0 else 0
    promedio_edades_mujeres = suma_edades_mujeres / total_mujeres if total_mujeres > 0 else 0
    return promedio_edades_hombres, promedio_edades_mujeres

def mostrar_resultados(total_personas, total_hombres, total_mujeres, promedio_edades_hombres, promedio_edades_mujeres, edad_minima):
    print("\n•••••••••••••••••••••••••••••••••••••••••")
    print(f"Total de personas: {total_personas}")
    print(f"Hombres: {total_hombres}")
    print(f"Mujeres: {total_mujeres}")
    print(f"Promedio de edades (Hombres): {promedio_edades_hombres:.2f}")
    print(f"Promedio de edades (Mujeres): {promedio_edades_mujeres:.2f}")
    print(f"Edad mínima: {edad_minima}")
    print("\n•••••••••••••••••••••••••••••••••••••••••")

def main():
    total_personas, total_hombres, total_mujeres, suma_edades_hombres, suma_edades_mujeres, edad_minima = obtener_datos_ingresados()
    promedio_edades_hombres, promedio_edades_mujeres = calcular_promedios(total_hombres, total_mujeres, suma_edades_hombres, suma_edades_mujeres)
    mostrar_resultados(total_personas, total_hombres, total_mujeres, promedio_edades_hombres, promedio_edades_mujeres, edad_minima)

main()
