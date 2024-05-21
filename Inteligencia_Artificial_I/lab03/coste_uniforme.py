# Clase Acción
class Accion:
  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre

#Clase Estado
class Estado:
  def __init__(self, nombre, acciones):
    self.nombre = nombre
    self.acciones = acciones

  def __str__(self):
    return self.nombre

#Clase Problema.
class Problema:
  def __init__(self, estado_inicial, estados_objetivos, acciones, costes=None):
    self.estado_inicial = estado_inicial
    self.estados_objetivos = estados_objetivos
    self.acciones = acciones
    self.costes = costes
    self.infinito = 99999
    # -- Si no se tiene costos, se inicializa todos los costos con 1
    if not self.costes:
      self.costes = {}
      for estado in self.acciones.keys():
        self.costes[estado] = {}
        for accion in self.acciones[estado].keys():
          self.costes[estado][accion] = 1

  def __str__(self):
    msg = "Estado Inicial: {0} -> Objetivos: {1}"
    return msg.format(self.estado_inicial.nombre,self.estados_objetivos)

  # -- Determina si se alcanzó el objetivo
  def es_objetivo(self, estado):
    return estado in self.estados_objetivos

  # -- Determina el estado al que se llega del estado actual en base a la acción
  def resultado(self, estado, accion):
    if estado.nombre not in self.acciones.keys():
      return None
    # -- Recuperar diccionario de posibles acciones que se pueden realizar del estado actual
    acciones_estado = self.acciones[estado.nombre]
    if accion.nombre not in acciones_estado.keys():
      return None
    # -- Recupera y devuelve el nuevo estado alcanzado después de ejecutar la acción
    return acciones_estado[accion.nombre]

  # -- Determina el costo de una acción de un estado
  def coste_accion(self, estado, accion):
    if estado.nombre not in self.costes.keys():
      return self.infinito
    costes_estado = self.costes[estado.nombre]
    if accion.nombre not in costes_estado.keys():
      return self.infinito
    return costes_estado[accion.nombre]

  # -- Determina el costo del camino desde la raiz a un nodo dado
  def coste_camino(self, nodo):
    total = 0
    while nodo.padre:
      total += self.coste_accion(nodo.padre.estado, nodo.accion)
      nodo = nodo.padre
    return total

class Nodo:
  def __init__(self, estado, accion=None, acciones=None, padre=None):
    self.estado = estado # -- Estado al que corresponde el nodo
    self.accion = accion # -- Acción mediante la cuál se llegó a este nodo
    self.acciones = acciones # -- Acciones posibles a realizar a partir de este nodo para llegar a los hijos
    self.padre = padre
    self.hijos = [] # -- Lista de nodos hijo (objetos) del nodo actual
    self.coste = 0

  def __str__(self):
    return self.estado.nombre

  # Método para expandir el nodo a los nodos hijo
  # -- Devuelve una lista de nodos hijo del nodo actual
  def expandir(self, problema):
    # -- Inicializar lista de nodos hijo
    self.hijos = []
    # -- Validar si el estado actual está o no en el contexto del problema
    if not self.acciones:
      if self.estado.nombre not in problema.acciones.keys():
        return self.hijos
      self.acciones = problema.acciones[self.estado.nombre]
    # -- Recuperar los nodos hijo en función a las acciones que se pueden realizar
    for accion in self.acciones.keys():
      accion_hijo = Accion(accion)
      nuevo_estado = problema.resultado(self.estado, accion_hijo)
      acciones_nuevo = {}
      if nuevo_estado.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nuevo_estado.nombre]
      hijo = Nodo(nuevo_estado, accion_hijo, acciones_nuevo, self)
      # -- Determinar el costo del hijo
      coste = self.padre.coste if self.padre else 0
      coste += problema.coste_accion(self.estado, accion_hijo)
      hijo.coste = coste
      self.hijos.append(hijo)
    # -- Devuelve la lista de nodos hijo
    return self.hijos

  # Método para seleccionar el hijo con el costo óptimo
  def hijo_mejor(self, problema):
    if not self.hijos:
      return None
    mejor = self.hijos[0]
    for hijo in self.hijos:
        # for objeto in problema.estados_objetivos:
        #     coste_camino_hijo = problema.coste_camino(hijo)
        #     coste_camino_mejor = problema.coste_camino(mejor)
        #     if(coste_camino_hijo < coste_camino_mejor):
        #         mejor = hijo
      if (hijo.coste < mejor.coste):
        mejor = hijo
    return mejor

def coste_uniforme(problema):
    # Crea el nodo raíz con el estado inicial del problema
    raiz = crea_nodo_raiz(problema)
    # Verifica si el estado inicial es un estado objetivo
    if problema.es_objetivo(raiz.estado):
      return raiz
    # Inicializa la frontera con el nodo raíz
    frontera = [raiz]
    # Inicializa el conjunto de estados explorados
    explorados = set()
    # Bucle principal de búsqueda
    while True:
      # Si la frontera está vacía, no se encontró solución
      if not frontera:
        return None
      # Extrae el nodo con menor costo de la frontera
      nodo = frontera.pop(0)
      # Si el nodo es un estado objetivo, retorna el nodo
      if problema.es_objetivo(nodo.estado):
          return nodo
      # Marca el estado del nodo como explorado
      explorados.add(nodo.estado)
      # Si no hay acciones disponibles desde este nodo, continúa con el siguiente
      if not nodo.acciones:
        continue
      # Expande el nodo generando nodos hijos para cada acción posible
      for nombre_accion in nodo.acciones.keys():
        accion =  Accion(nombre_accion)
        hijo = crea_nodo_hijo(problema, nodo, accion)
        # Si el estado del hijo no ha sido explorado ni está en la frontera, añádelo a la frontera
        estados_frontera = [nodo.estado for nodo in frontera]
        if (hijo.estado not in explorados and
            hijo.estado not in estados_frontera):
              frontera.append(hijo)
        else:
            # Si el estado del hijo ya está en la frontera, actualiza su costo si es menor
            buscar = [nodo for nodo in frontera
                      if nodo.estado == hijo.estado]
            if buscar:
                if hijo.coste < buscar[0].coste:
                    indice = frontera.index(buscar[0])
                    frontera[indice] = hijo
        # Ordena la frontera por costo
        frontera.sort(key=lambda nodo: nodo.coste)

def crea_nodo_raiz(problema):
    estado_raiz = problema.estado_inicial
    acciones_raiz = {}
    if estado_raiz.nombre in problema.acciones.keys():
      acciones_raiz = problema.acciones[estado_raiz.nombre]
    raiz = Nodo(estado_raiz, None, acciones_raiz, None)
    # El nodo raiz tiene coste 0
    raiz.coste = 0
    return raiz

def crea_nodo_hijo (problema, padre, accion):
    nuevo_estado = problema.resultado (padre.estado, accion)
    acciones_nuevo = {}
    if nuevo_estado.nombre in problema.acciones.keys():
      acciones_nuevo = problema.acciones[nuevo_estado.nombre]
    hijo = Nodo(nuevo_estado, accion, acciones_nuevo, padre)
    # Calcular el costo del nuevo nodo sumando el costo acumulado del padre y el costo de la acción
    coste = padre.coste
    coste += problema.coste_accion(padre.estado, accion)
    hijo.coste = coste
    padre.hijos.append(hijo)
    return hijo

def muestra_solucion(objetivo=None):
    if not objetivo:
      print('No hay solucion')
      return
    nodo = objetivo
    while nodo:
        # Imprime el estado y el costo total del nodo
        msg = "Estado: {0}, Coste Total: {1}"
        estado = nodo.estado.nombre
        coste_total = nodo.coste
        print(msg.format(estado, coste_total))
        # Si hay una acción que lleva a este estado, imprime la acción y su costo
        if nodo.accion:
            accion = nodo.accion.nombre
            padre = nodo.padre.estado
            coste = problema_resolver.coste_accion(padre, nodo.accion)
            msg = "<--- {0} [{1}]--->"
            print(msg.format(accion, coste))
        nodo = nodo.padre

if __name__ == "__main__":
    accN = Accion ('N')
    accS = Accion ('S')
    accE = Accion ('E')
    accO = Accion ('O')
    accNE = Accion ('NE')
    accNO = Accion ('NO')
    accSE = Accion ('SE')
    accSO = Accion ('SO')


    # -- Definción de estados
    lanoi = Estado('Lanoi', [accNE])
    nohoi = Estado ('Nohoi', [accSO, accNO, accNE])
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

    # -- Definición de viajes
    viajes = {'Lanoi': {'NE': nohoi},
              'Nohoi': {'SO': lanoi,
                        'NO': ruun,
                        'NE': milos},
              'Ruun' : {'NO': ghiido,
                        'NE': kuart,
                        'E': milos,
                        'SE': nohoi},
              'Milos' : {'O': ruun,
                          'SO': nohoi,
                          'N': khandan},
              'Ghiido' : {'N': nokshos,
                          'E': kuart,
                          'E': ruun,},
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

    costes = {'Lanoi': {'NE': 68},
              'Nohoi': {'SO': 121,
                        'NO': 187,
                        'NE': 55},
              'Ruun': {'NO': 95,
                       'NE': 34,
                       'E': 176,
                       'SE': 82},
              'Milos': {'O': 110,
                        'SO': 15,
                        'N': 77},
              'Ghiido': {'N': 43,
                         'E': 89,
                         'SE': 144},
              'Kuart': {'O': 58,
                        'SO': 122,
                        'NE': 190},
              'Boomon': {'N': 67,
                         'SO': 101},
              'Goorum': {'O': 121,
                         'S': 27},
              'Shiphos': {'O': 193,
                          'E': 41},
              'Nokshos': {'NO': 84,
                          'S': 175,
                          'E': 3},
              'Pharis': {'NO': 67,
                         'SO': 83},
              'Khamin': {'SE': 104,
                         'NO': 46,
                         'O': 71},
              'Tarios': {'O': 150,
                         'NO': 88,
                         'NE': 12,
                         'E': 134},
              'Peranna': {'O': 164,
                          'E': 121},
              'Khandan': {'O': 45,
                          'S': 28},
              'Tawa': {'SO': 199,
                       'SE': 73,
                       'NE': 122},
              'Theer': {'SO': 76,
                        'SE': 68},
              'Roria': {'NO': 147,
                        'SO': 93,
                        'E': 175},
              'Kosos': {'O': 189}
             }
    objetivo = [kosos]
    problema = Problema(lanoi, objetivo, viajes, costes)
    problema_resolver = problema
    solucion = coste_uniforme(problema_resolver)
    muestra_solucion(solucion)




