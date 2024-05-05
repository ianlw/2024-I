class Vehiculo:
    def __init__(self, Placa="", Marca="", Modelo="", Color="", Anio=""):
        self.Placa = Placa
        self.Marca = Marca
        self.Modelo = Modelo
        self.Color = Color
        self.Anio = Anio
        
    def Leer(self):
        print("\nIngresar los datos del vehículo")
        self.Placa = input("Placa: ")
        self.Marca = input("Marca: ")
        self.Modelo = input("Modelo: ")
        self.Color = input("Color: ")
        self.Anio = input("Anio: ")

    def Mostrar(self):
        print("\nDatos del vehículo")
        print("··················")
        print("Placa:", self.Placa)
        print("Marca:", self.Marca)
        print("Modelo:", self.Modelo)
        print("Color:", self.Color)
        print("Anio:", self.Anio)
    
    def Escribir(self, listaVehiculos):
        listaVehiculos.append(self)

class VehiculoCarga(Vehiculo):
    def __init__(self, Placa="", Marca="", Modelo="", Color="", Anio="", NroEjes="", CargaBruta="", CargaNeta=""):
        super().__init__(Placa, Marca, Modelo, Color, Anio)
        self.NroEjes = NroEjes
        self.CargaBruta = CargaBruta
        self.CargaNeta = CargaNeta

    def Leer(self):
        super().Leer()
        self.NroEjes = input("Número de ejes:")
        self.CargaBruta = input("Carga Bruta:")
        self.CargaNeta = input("Carga Neta:")

    def Mostrar(self):
        super().Mostrar()
        print("Número de ejes:", self.NroEjes)
        print("Carga Bruta:", self.CargaBruta)
        print("Carga Neta:", self.CargaNeta)
    
    def Escribir(self, listaVehiculos):
        listaVehiculos.append(self)
        
class VehiculoPasajeros(Vehiculo):
    def __init__(self, Placa="", Marca="", Modelo="", Color="", Anio="", NumPasajeros=""):
        super().__init__(Placa, Marca, Modelo, Color, Anio)
        self.NumPasajeros = NumPasajeros

    def Leer(self):
        super().Leer()
        self.NumPasajeros = input("Número de pasajeros: ")

    def Mostrar(self):
        super().Mostrar()
        print("Número de pasajeros:", self.NumPasajeros)

    def Escribir(self, listaVehiculos):
        listaVehiculos.append(self)

# Métodos del menú
def almacenarVehiculoCarga(listaVehiculos):
    vehiculo = VehiculoCarga()
    vehiculo.Leer()
    vehiculo.Escribir(listaVehiculos)

def almacenarVehiculoPasajeros(listaVehiculos):
    vehiculo = VehiculoPasajeros()
    vehiculo.Leer()
    vehiculo.Escribir(listaVehiculos)

def BuscarPorPlaca(listaVehiculos):
    placa = input("Ingrese la placa a buscar: ")
    print("------------------------------")
    flag = True
    for vehiculo in listaVehiculos:
        if vehiculo.Placa == placa:
            vehiculo.Mostrar()
            flag = False
    if flag:
        print("\nNo se encontró ningún vehículo con esa placa")
    print("------------------------------")

def MostrarTodosVehiculos(listaVehiculos):
    print("\nListado de todos los vehículos")
    print("------------------------------")
    for vehiculo in listaVehiculos:
        vehiculo.Mostrar()
    print("------------------------------")

def MostrarVehiculosCarga(listaVehiculos):
    print("\nListado de vehiculos de carga")
    print("------------------------------")
    for vehiculo in listaVehiculos:
        if isinstance(vehiculo, VehiculoCarga):
            vehiculo.Mostrar()
    print("-----------------------------")

def MostrarVehiculosPasajeros(listaVehiculos):
    print("\nListar los vehículos de pasajeros:")
    print("------------------------------")
    for vehiculo in listaVehiculos:
        if isinstance(vehiculo, VehiculoPasajeros):
            vehiculo.Mostrar()
    print("---------------------------------")

def menu():
    print("\n••••••")
    print(" Menú")
    print("••••••")
    print("1. Agregar vehículo de carga")
    print("2. Agregar vehículo de pasajeros")
    print("3. Mostrar datos de un vehículo por placa")
    print("4. Listar todos los vehículos")
    print("5. Listar vehículos de carga")
    print("6. Listar vehículos de pasajeros")
    print("7. Salir")

# Programa principal
def main():
    listaVehiculos = []

    # Ejemplo ya cargados en la lista 
    vehiculoCarga1 = VehiculoCarga("ABC123", "Toyota", "Hilux", "Blanco", "2022", "2", "5000", "4000")
    listaVehiculos.append(vehiculoCarga1)

    vehiculoCarga2 = VehiculoCarga("XYZ456", "Ford", "F-150", "Negro", "2023", "2", "6000", "4500")
    listaVehiculos.append(vehiculoCarga2)

    vehiculoCarga3 = VehiculoCarga("DEF789", "Chevrolet", "Silverado", "Rojo", "2021", "2", "5500", "4200")
    listaVehiculos.append(vehiculoCarga3)

    # Creamos y agregamos tres vehículos de pasajeros a la lista
    vehiculoPasajeros1 = VehiculoPasajeros("GHI123", "Honda", "Civic", "Gris", "2020", "5")
    listaVehiculos.append(vehiculoPasajeros1)

    vehiculoPasajeros2 = VehiculoPasajeros("JKL456", "Nissan", "Sentra", "Azul", "2019", "4")
    listaVehiculos.append(vehiculoPasajeros2)

    vehiculoPasajeros3 = VehiculoPasajeros("MNO789", "Toyota", "Corolla", "Negro", "2021", "5")
    listaVehiculos.append(vehiculoPasajeros3)

    while True:
        menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            almacenarVehiculoCarga(listaVehiculos)
        elif opcion == "2":
            almacenarVehiculoPasajeros(listaVehiculos)
        elif opcion == "3":
            BuscarPorPlaca(listaVehiculos)
        elif opcion == "4":
            MostrarTodosVehiculos(listaVehiculos)
        elif opcion == "5":
            MostrarVehiculosCarga(listaVehiculos)
        elif opcion == "6":
            MostrarVehiculosPasajeros(listaVehiculos)
        elif opcion == "7":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
