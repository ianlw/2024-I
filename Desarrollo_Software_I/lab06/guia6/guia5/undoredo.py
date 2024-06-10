import re

def es_expresion_correcta(expresion):
    # Eliminamos los espacios en blanco para simplificar la validación
    expresion = expresion.replace(" ", "")
    
    # Expresión regular para una expresión aritmética básica correcta
    patron = re.compile(r'^[\d\(\)][\d\+\-\*/\(\)]*[\d\)]$')
    
    # Verificamos si la expresión cumple con el patrón básico
    if not patron.match(expresion):
        return False
    
    # Verificamos si la expresión contiene operadores consecutivos incorrectos o colocaciones incorrectas
    if re.search(r'[\+\-\*/]{2,}', expresion) or re.search(r'^[\+\*/]', expresion) or re.search(r'[\+\-\*/]$', expresion):
        return False
    
    # Verificamos paréntesis balanceados
    balance = 0
    for char in expresion:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    if balance != 0:
        return False
    
    return True

# Pruebas
expresiones = ["12++3", "+12", "12+23+", "13+/12", "12+3", "12 + 23", "(12 + 3) * 4", "12 + (3 * 4)"]
resultados = {expresion: es_expresion_correcta(expresion) for expresion in expresiones}

print(resultados)
