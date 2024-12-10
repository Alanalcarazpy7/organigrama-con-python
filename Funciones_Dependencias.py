#   Agregar todas las dependendias de un organigrama a partir de un nodo(una dependencia especifica)
#   Al pasarle la raiz simplemente se agregaran todas las dependencias del organigrama
import pickle
from random import randint
import os


#   se crea la clase organigrama cuya raiz se la asignara posteriormente, la raiz sera un objeto de la clase Dependencia
class Organigrama:
    def __init__(self, COD, ORG, FEC):
        self.COD = COD
        self.ORG = ORG
        self.FEC = FEC
        self.raiz = None

    #   funcion para agregar una dependencia a la raiz, si la raiz ya existe se recorrera el organigrama con la funcion _agregar_dependencia
    def agregar_dependencia(self, COD, COD_SUPERIOR, NOMBRE, CODRES):
        NOMBRE = NOMBRE.strip()
        if NOMBRE != "":
            if self.raiz is None:
                self.raiz = Dependencia(COD, COD_SUPERIOR, NOMBRE, CODRES)
            else:
                lista_nombres = enlistar_nom_dependencias(self.raiz, [])
                _agregar_dependencia(COD, COD_SUPERIOR, NOMBRE, CODRES, self.raiz, lista_nombres)
    #   funcion para eliminar una dependencia, si la dependencia a eliminar  no es la raiz se recorre el organigrama con la funcion _eliminar_dependencia

    def eliminar_dependencia(self, COD):
        if self.raiz.COD == COD:
            self.raiz = None
        else:
            _eliminar_dependencia(self.raiz, COD)


#   Se crea la clase Dependencia, a esta clase se la llamara en las siguientes funciones con el nombre de NODO
class Dependencia:
    def __init__(self, COD, COD_SUPERIOR, NOMBRE, CODRES):
        self.COD = COD
        self.COD_SUCESOR = COD_SUPERIOR
        self.NOMBRE = NOMBRE
        self.CODRES = CODRES
        self.subdependencias = []


#   recorre recursivamente el organigrama (arbol) hasta encontrar el nodo cuyo codigo sea igual a COD_SUPERIOR,
#   donde se agregara una nueva dependencia a su lista de subdependencias
def _agregar_dependencia(COD, COD_SUPERIOR, NOMBRE, CODRES, NODO, lista_nombres):
    if NODO.COD == COD_SUPERIOR:
        contador = 1
        nom = NOMBRE
        while nom in lista_nombres:
            nom = NOMBRE + f"({contador})"
            contador = contador + 1
        NODO.subdependencias.append(Dependencia(COD, COD_SUPERIOR, nom, CODRES))
    else:
        for NODO in NODO.subdependencias:
            _agregar_dependencia(COD, COD_SUPERIOR, NOMBRE, CODRES, NODO, lista_nombres)


#   eliminar una dependencia de codigo igual a COD y retorna la dependencia eliminada
def _eliminar_dependencia(NODO, COD):
    for indice_subnodo in range(len(NODO.subdependencias)):     # Recorrer toda la lista de subdependencias de una Dependencia
        if NODO.subdependencias[indice_subnodo].COD == COD:
            auxiliar = NODO.subdependencias[indice_subnodo]
            NODO.subdependencias.pop(indice_subnodo)            # Quitar la dependencia a eliminar de la lista de subdependencias de su superior
            return auxiliar
            # Retornar la dependencia(Nodo) eliminado
    for subnodo in NODO.subdependencias:
        eliminado = _eliminar_dependencia(subnodo, COD)
        if eliminado:
            return eliminado
    return None


#   Funcion para mover una dependencia
def mover_dependencia(NODO, COD_a_mover, COD_destino):
    nodo = _eliminar_dependencia(NODO, COD_a_mover)     # Elimina el NODO identificado con el codigo
    _mover_dependencia(NODO, nodo, COD_destino)         # copia ese nodo a la lista de subdependencias del nodo destino


def _mover_dependencia(NODO_raiz, NODO_a_mover, COD_destino):
    if NODO_raiz.COD == COD_destino:
        NODO_raiz.subdependencias.append(NODO_a_mover)
    else:
        for sub in NODO_raiz.subdependencias:
            _mover_dependencia(sub, NODO_a_mover, COD_destino)


#   Funcion para modificar el  jefe de una dependencia
def cambiar_jefe_dep(NODO, dep_modificada_COD, nuevojefe_CI):
    if NODO.COD == dep_modificada_COD:
        NODO.CODRES = nuevojefe_CI
    else:
        for subdependencia in NODO.subdependencias:
            cambiar_jefe_dep(subdependencia, dep_modificada_COD, nuevojefe_CI)


#   Funcion para modificar el nombre de una dependencia
def modificar_nombre_dep(NODO, DEP_A_EDITAR, N_NOMBRE, codigo_org):
    N_NOMBRE = N_NOMBRE.strip()
    if NODO.COD == DEP_A_EDITAR:
        contador = 1
        nom = N_NOMBRE
        organigrama_actual = cargar_dependencia_organigrama(codigo_org)

        while nom in enlistar_nom_dependencias(organigrama_actual.raiz, []):
            nom = N_NOMBRE + f"({contador})"
            contador = contador + 1
        NODO.NOMBRE = nom
        return nom
    else:
        for sub in NODO.subdependencias:
            nom = modificar_nombre_dep(sub, DEP_A_EDITAR, N_NOMBRE, codigo_org)
            if nom is not None:
                return nom


#   Retorna una matriz con el nombre y codigo de cada dependencia
def matriz_nombre_codigo(NODO, matriz):
    if NODO is None:
        return []
    matriz.append([NODO.NOMBRE, NODO.COD])
    for subNODO in NODO.subdependencias:
        matriz_nombre_codigo(subNODO, matriz)
    return matriz


#   Enlista el nombre de todas las dependencias a partir de un nodo
def enlistar_nom_dependencias(NODO, listadependencias):
    if NODO is None:
        return []
    listadependencias.append(NODO.NOMBRE)
    for subNODO in NODO.subdependencias:
        enlistar_nom_dependencias(subNODO, listadependencias)
    return listadependencias


#   Enlista el codigo de todas las dependencias a partir de un nodo
def enlistar_cod_dependencias(NODO, listadependencias_cod):
    if NODO is None:
        return []
    listadependencias_cod.append(NODO.COD)
    for subNODO in NODO.subdependencias:
        enlistar_cod_dependencias(subNODO, listadependencias_cod)
    return listadependencias_cod


#   Enlista todas las dependendias de un organigrama a partir de un nodo(una dependencia especifica) definida por el codigo
#   Al pasarle la raiz simplemente se agregaran todas las dependencias del organigrama
def enlistar_nom_nodo(NODO, COD, lista):
    if NODO is None:
        return []
    if NODO.COD == COD:
        enlistar_nom_dependencias(NODO, lista)
    else:
        for subNODO in NODO.subdependencias:
            enlistar_nom_nodo(subNODO, COD, lista)
    return lista


def enlistar_cod_nodo(NODO, COD, lista):
    if NODO is None:
        return []
    if NODO.COD == COD:
        enlistar_cod_dependencias(NODO, lista)
    else:
        for subNODO in NODO.subdependencias:
            enlistar_cod_nodo(subNODO, COD, lista)
    return lista


#   Funcion para buscar el nombre de una persona de acuerdo a su codigo en la lista de personales
def get_nom_persona(Codigo, Personales):
    if not Personales or Personales is None:
        return ""
    else:
        for persona in Personales:
            if persona[2] == Codigo:
                return persona[0] + " " + persona[1]
        return ""


# funcion para mostrar las dependencias que son cadidatas a ser superior de otra
# no son candidatas 1) la misma dependencia 2) sus subdependencias
def superiores_disponibles(NODO, COD):
    Totalidad = matriz_nombre_codigo(NODO, [])
    no_candidatas = enlistar_cod_nodo(NODO, COD, [])
    Candidatas = []
    for elemento in Totalidad:
        if elemento[1] not in no_candidatas:
            Candidatas.append(elemento)
    return Candidatas


# estas dos funciones se usan para generar las listas que necesita graphviz para graficar
def lista_grafica(NODO, lista_empleados, inicio, fin):
    NODO_jefe = ""
    if lista_empleados is not None:
        for empleado in lista_empleados:
            if empleado[2] == NODO.CODRES and empleado[8] == NODO.COD:
                NODO_jefe = empleado[0] + " " + empleado[1]
    if NODO_jefe == "":
        NODO_jefe = "(No asignado)"
    for sub in NODO.subdependencias:
        sub_jefe = ""
        if lista_empleados is not None:
            for empleado in lista_empleados:
                if empleado[2] == sub.CODRES and empleado[8] == sub.COD:
                    sub_jefe = empleado[0] + " " + empleado[1]
        if sub_jefe == "":
            sub_jefe = "(No asignado)"
        inicio.append(NODO.NOMBRE + f"\n{NODO_jefe}")
        fin.append(sub.NOMBRE + f"\n{sub_jefe}")
    for sub in NODO.subdependencias:
        lista_grafica(sub, lista_empleados, inicio, fin)
    return [inicio, fin]


def gen_lista_grafica(COD, NODO, lista_empleados):
    if NODO is None:
        return [[], []]
    if COD == NODO.COD:
        return lista_grafica(NODO, lista_empleados, [], [])
    else:
        for sub in NODO.subdependencias:
            rec = gen_lista_grafica(COD, sub, lista_empleados)  # se usa la variable rec para almacenar el resultado de la recursion
            if rec is not None:
                return rec


# Funcion para obtener el nombre de la dependencia de acuerdo a su codigo
def get_nom(NODO, COD):
    if NODO is None:
        return None
    if COD == NODO.COD:
        return NODO.NOMBRE
    for sub in NODO.subdependencias:
        Rec = get_nom(sub, COD)
        if Rec is not None:
            return Rec


def mostrar_dependencias_sucesoras(nombre_dependencia, raiz_organigrama):
    dependencia_encontrada = buscar_dependencia(nombre_dependencia, raiz_organigrama)
    dependencias_sucesoras = enlistar_nom_dependencias(dependencia_encontrada, [])
    return dependencias_sucesoras


#   funcion para buscar una dependencia y que retorne
def buscar_dependencia(nombre_dependencia, nodo_actual):
    if nodo_actual is None:
        return None
    if nodo_actual.NOMBRE == nombre_dependencia:
        return nodo_actual
    for subdependencia in nodo_actual.subdependencias:
        resultado = buscar_dependencia(nombre_dependencia, subdependencia)
        if resultado is not None:
            return resultado
    return None


#   Retorna el nombre del jefe de una dependencia, si la dependencia no tiene jefe, retorna None
def obtener_jefe(NODO, COD, Personales):
    if not Personales or Personales is None or COD is None:
        return ""
    elif NODO.COD == COD:
        return get_nom_persona(NODO.CODRES, Personales)
    else:
        for sub in NODO.subdependencias:
            jefe = obtener_jefe(sub, COD, Personales)
            if jefe is not None:
                return jefe


#Funciones para guardar y cargar una lista con los datos de los organigramas (codigo, nombre, fecha)
def guardar_nombres_organigrama(organigramas):
    with open('nombres_organigramas', 'wb') as archivo:
        pickle.dump(organigramas, archivo)  # Guardar la lista completa


def cargar_nombres_organigramas():
    try:
        with open('nombres_organigramas', 'rb') as archivo:
            organigramas = pickle.load(archivo)
        return organigramas
    except FileNotFoundError:
        return []  # Devolver lista vacía si no se encuentra el archivo


#Funciones para guardar, cargar y eliminar las entidades de organigramas contenidos en los archivos organigrama{codigo_org}_dependencias
def cargar_dependencia_organigrama(codigo_org):
    try:
        file_path = os.path.join("archivos_organigramas", f'organigrama{codigo_org}_dependencias')
        with open(file_path, 'rb') as archivo:
            organigrama_actual = pickle.load(archivo)
        return organigrama_actual
    except FileNotFoundError:
        return None


def guardar_dependencia_organigrama(codigo_org, Organigrama_a_guardar):
    # Verificar si la carpeta "archivos_organigramas" existe, de lo contrario, crearla
    if not os.path.exists("archivos_organigramas"):
        os.makedirs("archivos_organigramas")
    file_path = os.path.join("archivos_organigramas", f'organigrama{codigo_org}_dependencias')
    with open(file_path, 'wb') as archivo:
        pickle.dump(Organigrama_a_guardar, archivo)


def eliminar_archivo_organigrama(codigo_org):
    import os
    # Especifica la ruta y nombre del archivo a eliminar
    file_path = os.path.join("archivos_organigramas", f'organigrama{codigo_org}_dependencias')
    try:
        # Intenta eliminar el archivo
        os.remove(file_path)
    except OSError as e:
        pass


#Funciones para cargar guardar y eliminar los archivos de personales de distintos organigramas
def eliminar_archivo_personas(codigo_org):
    import os
    # Especifica la ruta y nombre del archivo a eliminar
    file_path = os.path.join("archivos_personas", f'organigrama{codigo_org}_personas')
    try:
        # Intenta eliminar el archivo
        os.remove(file_path)
    except OSError as e:
        pass

#Carga las personas que existen en el organigrama
def cargar_personas_organigrama(codigo_org):
    try:
        file_path = os.path.join("archivos_personas", f'organigrama{codigo_org}_personas')
        with open(file_path, 'rb') as archivo:
            matriz_personas = pickle.load(archivo)
        return matriz_personas
    except FileNotFoundError:
        return None


#Verificar si la carpeta "archivos_organigramas" existe, de lo contrario, crearla
def guardar_personas_organigrama(codigo_org, matriz_personas):
    if not os.path.exists("archivos_personas"):
        os.makedirs("archivos_personas")
    file_path = os.path.join("archivos_personas", f'organigrama{codigo_org}_personas')
    with open(file_path, 'wb') as archivo:
        pickle.dump(matriz_personas, archivo)


#Funciones para generar los codigos aleatorios de las dependencias
def generar_codigo_dep(NODO):
    lista_codigos = enlistar_cod_dependencias(NODO, [])
    encontrado = 0
    while encontrado == 0:
        codigo_aleatorio = randint(0, 999)
        if codigo_aleatorio not in lista_codigos:
            encontrado = 1
    codigo_aleatorio = str(codigo_aleatorio)
    while len(codigo_aleatorio) < 3:
        codigo_aleatorio = "0" + codigo_aleatorio
    return codigo_aleatorio

#Enlista todos los codigos del organigrama
def lista_codigos_ORG(LISTA):
    codigos = []
    for org in LISTA:
        codigos.append(org[0])
    return codigos

#Funcion para generar los codigos aleatorios del organigrama
def generar_codigo_ORG(LISTA_ORG):
    lista_codigos = lista_codigos_ORG(LISTA_ORG)
    encontrado = 0
    while encontrado == 0:
        codigo_aleatorio = randint(0, 99999)
        if codigo_aleatorio not in lista_codigos:
            encontrado = 1
    codigo_aleatorio = str(codigo_aleatorio)
    while len(codigo_aleatorio) < 5:
        codigo_aleatorio = "0" + codigo_aleatorio
    return codigo_aleatorio
