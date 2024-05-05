def calcular_utilidad(salario_mensual, antiguedad):
    if antiguedad < 1:
        utilidad = salario_mensual * 0.05
    elif antiguedad < 2:
        utilidad = salario_mensual * 0.07
    elif antiguedad < 5:
        utilidad = salario_mensual * 0.10
    elif antiguedad < 10:
        utilidad = salario_mensual * 0.15
    else:
        utilidad = salario_mensual * 0.20
    return utilidad

def main():
    salario_mensual = float(input("Ingrese el salario mensual: "))
    antiguedad = float(input("Ingrese los años de trabajo: "))
    utilidad = calcular_utilidad(salario_mensual, antiguedad)
    print("La utilidad del trabajador es:", utilidad, "Nuevos Soles")

if __name__ == "__main__":
    main()
