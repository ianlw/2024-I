# Función para obtener el alumno con la mayor nota
def alumno_mayor_nota(estudiantes):
    mejor_alumno = None
    mejor_nota = -1
    for estudiante in estudiantes:
        if estudiante['nota'] > mejor_nota:
            mejor_nota = estudiante['nota']
            mejor_alumno = estudiante
    return mejor_alumno

# Función para contar el número de alumnos con nota mayor a 16
def contar_alumnos_mayor_a_16(estudiantes):
    contador = 0
    for estudiante in estudiantes:
        if estudiante['nota'] > 16:
            contador += 1
    return contador

# Función para obtener la alumna con la menor nota
def alumna_menor_nota(estudiantes):
    peor_alumna = None
    peor_nota = 21
    for estudiante in estudiantes:
        if estudiante['sexo'] == 'F' and estudiante['nota'] < peor_nota:
            peor_nota = estudiante['nota']
            peor_alumna = estudiante
    return peor_alumna

# Función para calcular el promedio de las notas desaprobadas
def calcular_promedio_desaprobadas(estudiantes):
    suma_desaprobadas = 0
    cantidad_desaprobadas = 0
    for estudiante in estudiantes:
        if estudiante['nota'] < 14:
            suma_desaprobadas += estudiante['nota']
            cantidad_desaprobadas += 1
    if cantidad_desaprobadas == 0:
        return 0
    return suma_desaprobadas / cantidad_desaprobadas

# Número de alumnos
n = int(input("Ingrese el número de alumnos: "))

# Lista para almacenar los datos de los estudiantes
estudiantes = []

# Leer datos de los estudiantes
for i in range(n):
    codigo = int(input("Ingrese el código del estudiante: "))
    
    # Validar que la nota esté entre 0 y 20
    while True:
        nota = float(input("Ingrese la nota del estudiante (0 a 20): "))
        if 0 <= nota <= 20:
            break
        else:
            print("La nota ingresada no está en el rango válido. Por favor, ingrese una nota entre 0 y 20.")
    
    sexo = input("Ingrese el sexo del estudiante (M/F): ").upper()
    
    # Validar que el sexo sea M o F
    while sexo != 'M' and sexo != 'F':
        print("Sexo no válido. Por favor, ingrese M para masculino o F para femenino.")
        sexo = input("Ingrese el sexo del estudiante (M/F): ").upper()
    
    estudiantes.append({'codigo': codigo, 'nota': nota, 'sexo': sexo})

# Mostrar el alumno con la mayor nota
mejor_alumno = alumno_mayor_nota(estudiantes)
print("El alumno con la mayor nota es:", mejor_alumno['codigo'], "con nota", mejor_alumno['nota'])

# Mostrar el número de alumnos que tienen nota mayor a 16
cantidad_alumnos_mayor_a_16 = contar_alumnos_mayor_a_16(estudiantes)
print("El número de alumnos con nota mayor a 16 es:", cantidad_alumnos_mayor_a_16)

# Mostrar la alumna con la menor nota
peor_alumna = alumna_menor_nota(estudiantes)
if peor_alumna:
    print("La alumna con la menor nota es:", peor_alumna['codigo'], "con nota", peor_alumna['nota'])
else:
    print("No hay alumnas en el conjunto de estudiantes.")

# Mostrar el promedio de las notas desaprobadas (<14)
promedio_desaprobadas = calcular_promedio_desaprobadas(estudiantes)
print("El promedio de las notas desaprobadas es:", promedio_desaprobadas)

