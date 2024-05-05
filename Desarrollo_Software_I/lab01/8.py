def clasificar_persona(edad):
    if edad < 18:
        return "Menor de Edad"
    elif 18 <= edad <= 60:
        return "Adulto"
    else:
        return "Adulto Mayor"

def main():
    cantidad_menores = 0
    suma_edades_menores = 0
    cantidad_adultos = 0
    suma_edades_adultos = 0
    cantidad_mayores = 0
    suma_edades_mayores = 0
    
    num_personas = int(input("Ingrese el número de personas: "))
    
    for i in range(num_personas):
        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
        clasificacion = clasificar_persona(edad)
        
        if clasificacion == "Menor de Edad":
            cantidad_menores += 1
            suma_edades_menores += edad
        elif clasificacion == "Adulto":
            cantidad_adultos += 1
            suma_edades_adultos += edad
        else:
            cantidad_mayores += 1
            suma_edades_mayores += edad
    
    if cantidad_menores > 0:
        promedio_menores = suma_edades_menores / cantidad_menores
        print("Cantidad de Menores de Edad:", cantidad_menores)
        print("Promedio de edad de Menores de Edad:", promedio_menores)
    else:
        print("No se ingresaron Menores de Edad.")
    
    if cantidad_adultos > 0:
        promedio_adultos = suma_edades_adultos / cantidad_adultos
        print("Cantidad de Adultos:", cantidad_adultos)
        print("Promedio de edad de Adultos:", promedio_adultos)
    else:
        print("No se ingresaron Adultos.")
    
    if cantidad_mayores > 0:
        promedio_mayores = suma_edades_mayores / cantidad_mayores
        print("Cantidad de Adultos Mayores:", cantidad_mayores)
        print("Promedio de edad de Adultos Mayores:", promedio_mayores)
    else:
        print("No se ingresaron Adultos Mayores.")

if __name__ == "__main__":
    main()
