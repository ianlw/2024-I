def calcular_comision(ventas_totales):
    if ventas_totales <= 150:
        comision = 0
    elif ventas_totales <= 400:
        comision = ventas_totales * 0.10
    else:
        comision = 50 + (ventas_totales * 0.09)
    return comision

def main():
    ventas_totales = float(input("Ingrese el monto de las ventas totales: "))
    comision = calcular_comision(ventas_totales)
    print("La comisión es:", comision)

main()
