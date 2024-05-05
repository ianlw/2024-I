pago_diario = 50  # Pago diario 

# Función para calcular el sueldo mensual de un empleado
def calcular_sueldo_mensual(dias_trabajados, faltas):
    sueldo_mensual = (dias_trabajados - faltas) * pago_diario
    return sueldo_mensual

# Función para procesar los empleados  
def procesar_empleados(N):
    monto_total_sueldos = 0
    empleados_2500_3500 = 0
    empleados_menos_1000_mas_4000 = 0

    for i in range(1, N+1):
        nombre = input("Ingrese el nombre del empleado {}: ".format(i))
        dias_trabajados = int(input("Ingrese el número de días trabajados por {}: ".format(nombre)))
        faltas = int(input("Ingrese el número de faltas de {}: ".format(nombre)))

        sueldo_mensual = calcular_sueldo_mensual(dias_trabajados, faltas)

        monto_total_sueldos += sueldo_mensual

        if 2500 <= sueldo_mensual <= 3500:
            empleados_2500_3500 += 1

        if sueldo_mensual < 1000 or sueldo_mensual > 4000:
            empleados_menos_1000_mas_4000 += 1

    return monto_total_sueldos, empleados_2500_3500, empleados_menos_1000_mas_4000

def main():
    N = int(input("Ingrese el número de empleados: "))
    monto_total_sueldos, empleados_2500_3500, empleados_menos_1000_mas_4000 = procesar_empleados(N)

    print("\nMonto total de sueldos de todos los empleados:", monto_total_sueldos)
    print("Número de empleados que ganan entre 2500 y 3500:", empleados_2500_3500)
    print("Número de empleados que ganan menos de 1000 o más de 4000:", empleados_menos_1000_mas_4000)

# Llamada a la función principal
if __name__ == "__main__":
    main()

