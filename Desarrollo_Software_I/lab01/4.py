def calcular_salario_total(horas_trabajadas, tarifa_hora):
    if horas_trabajadas <= 40:
        salario_total = horas_trabajadas * tarifa_hora
    else:
        horas_normales = 40
        horas_extra = horas_trabajadas - horas_normales

        if horas_extra <= 8:
            salario_extra = horas_extra * (2 * tarifa_hora)
        else:
            salario_extra = 8 * (2 * tarifa_hora) + (horas_extra - 8) * (3 * tarifa_hora)

        salario_total = horas_normales * tarifa_hora + salario_extra

    return salario_total

def main():
    horas_trabajadas = float(input("Ingrese el total de horas trabajadas: "))
    tarifa_hora = float(input("Ingrese el pago por hora: "))
    salario_total = calcular_salario_total(horas_trabajadas, tarifa_hora)
    print("El salario total del trabajador es: ", salario_total, "Nuevos Soles")

main()
