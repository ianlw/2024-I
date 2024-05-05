

def calcular_descuento(monto_compra):
    if monto_compra > 5000:
        descuento = monto_compra * 0.30
    elif monto_compra > 3000:
        descuento = monto_compra * 0.20
    elif monto_compra > 1000:
        descuento = monto_compra * 0.10
    else:
        descuento = 0
    return descuento

def main():
    monto_compra = int(input("Ingrese el monto de compra: "))
    descuento = calcular_descuento(monto_compra)
    print("El monto de descuento es:", descuento)

if __name__ == "__main__":
    main()
