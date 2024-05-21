import heapq

class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Estado:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

    def __str__(self):
        return self.nombre

class Problema:
    def __init__(self, estado_inicial, estados_objetivos, acciones, costes=None):
        self.estado_inicial = estado_inicial
        self.estados_objetivos = estados_objetivos
        self.acciones = acciones
        self.costes = costes
        self.infinito = 99999
        if not self.costes:
            self.costes = {}
            for estado in self.acciones.keys():
                self.costes[estado] = {}
                for accion in self.acciones[estado].keys():
                    self.costes[estado][accion] = 1

    def __str__(self):
        msg = "Estado Inicial: {0} -> Objetivos: {1}"
        return msg.format(self.estado_inicial.nombre, self.estados_objetivos)

    def es_objetivo(self, estado):
        return estado in self.estados_objetivos

    def resultado(self, estado, accion):
        if estado.nombre not in self.acciones.keys():
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre]

    def coste_accion(self, estado, accion):
        if estado.nombre not in self.costes.keys():
            return self.infinito
        costes_estado = self.costes[estado.nombre]
        if accion.nombre not in costes_estado.keys():
            return self.infinito
        return costes_estado[accion.nombre]

    def coste_camino(self, nodo):
        total = 0
        while nodo.padre:
            total += self.coste_accion(nodo.padre.estado, nodo.accion)
            nodo = nodo.padre
        return total

class Nodo:
    def __init__(self, estado, accion=None, acciones=None, padre=None):
        self.estado = estado
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijos = []
        self.coste = 0

    def __str__(self):
        return self.estado.nombre

    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones = problema.acciones[self.estado.nombre]
        for accion in self.acciones.keys():
            accion_hijo = Accion(accion)
            nuevo_estado = problema.resultado(self.estado, accion_hijo)
            acciones_nuevo = {}
            if nuevo_estado.nombre in problema.acciones.keys():
                acciones_nuevo = problema.acciones[nuevo_estado.nombre]
            hijo = Nodo(nuevo_estado, accion_hijo, acciones_nuevo, self)
            coste = self.coste + problema.coste_accion(self.estado, accion_hijo)
            hijo.coste = coste
            self.hijos.append(hijo)
        return self.hijos

    def hijo_mejor(self, problema):
        if not self.hijos:
            return None
        mejor = self.hijos[0]
        for hijo in self.hijos:
            if hijo.coste < mejor.coste:
                mejor = hijo
        return mejor

    def __lt__(self, other):
        return self.coste < other.coste

    def __eq__(self, other):
        return self.coste == other.coste

class ViajesCiudades:
    def __init__(self):
        self.nombre = 'Viajes por ciudades'
        accN = Accion('N')
        accS = Accion('S')
        accE = Accion('E')
        accO = Accion('O')
        accNE = Accion('NE')
        accNO = Accion('NO')
        accSE = Accion('SE')
        accSO = Accion('SO')

        lanoi = Estado('Lanoi', [accNE])
        nohoi = Estado('Nohoi', [accSO, accNO, accNE])
        ruun = Estado('Ruun', [accNO, accNE, accE, accSE])
        milos = Estado('Milos', [accO, accSO, accN])
        ghiido = Estado('Ghiido', [accN, accE, accSE])
        kuart = Estado('Kuart', [accO, accSO, accNE])
        boomon = Estado('Boomon', [accN, accSO])
        goorum = Estado('Goorum', [accO, accS])
        shiphos = Estado('Shiphos', [accO, accE])
        nokshos = Estado('Nokshos', [accNO, accS, accE])
        pharis = Estado('Pharis', [accNO, accSO])
        khamin = Estado('Khamin', [accSE, accNO, accO])
        tarios = Estado('Tarios', [accO, accNO, accNE, accE])
        peranna = Estado('Peranna', [accO, accE])
        khandan = Estado('Khandan', [accO, accS])
        tawa = Estado('Tawa', [accSO, accSE, accNE])
        theer = Estado('Theer', [accSO, accSE])
        roria = Estado('Roria', [accNO, accSO, accE])
        kosos = Estado('Kosos', [accO])

        viajes = {'Lanoi': {'NE': nohoi},
                  'Nohoi': {'SO': lanoi,
                            'NO': ruun,
                            'NE': milos},
                  'Ruun': {'NO': ghiido,
                           'NE': kuart,
                           'E': milos,
                           'SE': nohoi},
                  'Ghiido': {'N': nokshos,
                             'E': kuart,
                             'SE': ruun},
                  'Milos': {'O': ruun,
                            'SO': nohoi,
                            'N': khandan},
                  'Kuart': {'O': ghiido,
                            'SO': ruun,
                            'NE': boomon},
                  'Boomon': {'N': goorum,
                             'SO': kuart},
                  'Goorum': {'O': shiphos,
                             'S': boomon},
                  'Shiphos': {'O': nokshos,
                              'E': goorum},
                  'Nokshos': {'NO': pharis,
                              'S': ghiido,
                              'E': shiphos},
                  'Pharis': {'NO': khamin,
                             'SO': nokshos},
                  'Khamin': {'SE': pharis,
                             'NO': tawa,
                             'O': tarios},
                  'Tarios': {'O': khamin,
                             'NO': tawa,
                             'NE': roria,
                             'E': peranna},
                  'Peranna': {'O': tarios,
                              'E': khandan},
                  'Khandan': {'O': peranna,
                              'S': milos},
                  'Tawa': {'SO': khamin,
                           'SE': tarios,
                           'NE': theer},
                  'Theer': {'SO': tawa,
                            'SE': roria},
                  'Roria': {'NO': theer,
                            'SO': tarios,
                            'E': kosos},
                  'Kosos': {'O': roria}
                  }

        self.estados = [lanoi, nohoi, ruun, milos, ghiido, kuart, boomon, goorum,
                        shiphos, nokshos, pharis, khamin, tarios, peranna, khandan,
                        tawa, theer, roria, kosos]
        self.viajes = viajes
        self.costes = {
            'Lanoi': {'NE': 2},
            'Nohoi': {'SO': 2, 'NO': 3, 'NE': 1},
            'Ruun': {'NO': 2, 'NE': 2, 'E': 2, 'SE': 3},
            'Ghiido': {'N': 3, 'E': 1, 'SE': 2},
            'Milos': {'O': 3, 'SO': 2, 'N': 1},
            'Kuart': {'O': 1, 'SO': 2, 'NE': 2},
            'Boomon': {'N': 1, 'SO': 2},
            'Goorum': {'O': 2, 'S': 2},
            'Shiphos': {'O': 1, 'E': 2},
            'Nokshos': {'NO': 2, 'S': 1, 'E': 2},
            'Pharis': {'NO': 3, 'SO': 2},
            'Khamin': {'SE': 2, 'NO': 1, 'O': 2},
            'Tarios': {'O': 3, 'NO': 2, 'NE': 1, 'E': 2},
            'Peranna': {'O': 2, 'E': 1},
            'Khandan': {'O': 3, 'S': 2},
            'Tawa': {'SO': 2, 'SE': 1, 'NE': 2},
            'Theer': {'SO': 2, 'SE': 1},
            'Roria': {'NO': 2, 'SO': 3, 'E': 2},
            'Kosos': {'O': 1}
        }

    def __str__(self):
        return self.nombre

    def crea_nodo_raiz(self, problema):
        estado_raiz = problema.estado_inicial
        acciones_raiz = {}
        if estado_raiz.nombre in problema.acciones.keys():
            acciones_raiz = problema.acciones[estado_raiz.nombre]
        raiz = Nodo(estado_raiz, None, acciones_raiz, None)
        return raiz

    def crea_nodo_hijo(self, problema, padre, accion):
        nuevo_estado = problema.resultado(padre.estado, accion)
        acciones_nuevo = {}
        if nuevo_estado.nombre in problema.acciones.keys():
            acciones_nuevo = problema.acciones[nuevo_estado.nombre]
        hijo = Nodo(nuevo_estado, accion, acciones_nuevo, padre)
        padre.hijos.append(hijo)
        return hijo

    def mostrar_nodo_padre(self, nodo):
        if nodo.padre:
            self.mostrar_nodo_padre(nodo.padre)
            print()
            print('--------------------------------')
            print('Se partió de la ciudad:', nodo.padre.estado.nombre)
            print('Se realizó la acción:', nodo.accion.nombre)
            print('Se llegó a la ciudad:', nodo.estado.nombre)

    def muestra_solucion(self, objetivo=None):
        if not objetivo:
            print('No hay solucion')
            return
        
        nodo_actual = objetivo
        while nodo_actual.padre:
            costo_accion = nodo_actual.padre.coste_camino(nodo_actual)
            print('--------------------------------')
            print('Se partió de la ciudad:', nodo_actual.padre.estado.nombre)
            print('Se realizó la acción:', nodo_actual.accion.nombre, 'con un costo de:', costo_accion)
            print('Se llegó a la ciudad:', nodo_actual.estado.nombre, 'con un coste total de:', nodo_actual.coste)
            nodo_actual = nodo_actual.padre

    def ucs(self, problema):
        raiz = self.crea_nodo_raiz(problema)
        if problema.es_objetivo(raiz.estado):
            return raiz

        frontera = []
        heapq.heappush(frontera, (0, raiz))

        explorados = set()

        while frontera:
            coste, nodo = heapq.heappop(frontera)

            if problema.es_objetivo(nodo.estado):
                return nodo

            explorados.add(nodo.estado)

            for hijo in nodo.expandir(problema):
                if hijo.estado not in explorados:
                    heapq.heappush(frontera, (hijo.coste, hijo))

        return None

    def DeterminarRuta(self):
        ciudad_inicial = input('Ingrese ciudad de partida: ')
        ciudad_destino = input('Ingrese ciudad de destino: ')
        estado_inicial = next((e for e in self.estados if e.nombre == ciudad_inicial), None)
        estados_objetivo = [e for e in self.estados if e.nombre == ciudad_destino]

        if not estado_inicial:
            print("La ciudad de partida no existe en la lista de ciudades.")
            return

        if not estados_objetivo:
            print("La ciudad de destino no existe en la lista de ciudades.")
            return

        problema = Problema(estado_inicial, estados_objetivo, self.viajes, self.costes)
        solucion = self.ucs(problema)
        self.muestra_solucion(solucion)

viaje_ciudades = ViajesCiudades()
viaje_ciudades.DeterminarRuta()
