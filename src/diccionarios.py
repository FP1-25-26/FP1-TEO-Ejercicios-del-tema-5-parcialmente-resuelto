from collections import Counter


def sustituye_palabras(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    palabras = texto.split()
    res = ""
    for p in palabras:
        # Se podría sustituir el if...else por esto:
        # res += diccionario.get(p, p)
        if p in diccionario:
            # p está en el diccionario, hay que sustituirla
            res += diccionario[p] + " "
        else:
            # hay que dejar la palabra tal cual
            res += p + " "
    return res.strip()

def sustituye_palabras_2(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    palabras = texto.split()
    res = []
    for p in palabras:
        if p in diccionario:
            # p está en el diccionario, hay que sustituirla
            res.append(diccionario[p]) 
        else:
            # hay que dejar la palabra tal cual
            res.append(p)
    return " ".join(res)

def sustituye_palabras_3(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    for p1, p2 in diccionario.items():
        texto = texto.replace(p1, p2)
    return texto

def indexa_por_iniciales(texto: str) -> dict[str, set[str]]:
    """
    Construye un diccionario que indexa las distintas palabras del texto
    (pasado a minúsculas) por sus iniciales.
    
    Parámetros:
        texto: Texto del que se van a extraer las palabras.
    
    Devuelve:
        Diccionario que asocia a cada inicial el conjunto de palabras
         que comienzan por dicha inicial.
    
    """
    # TODO: Intentar resolver usando un defaultdict(set)
    # Dividimos la cadena en palabras (los trozos separados por espacio)
    palabras = texto.lower().split()
    res = {}
    for p in palabras:
        inicial = p[0]
        if inicial not in res:
            res[inicial] = set()
        res[inicial].add(p)
    return res


def construye_frecuencias_bigramas(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    conteos = {}
    texto = texto.lower()
    # TODO: Intentar resolver sin zip, usando range
    for c1, c2 in zip(texto, texto[1:]):
        bigrama = c1 + c2
        if bigrama.isalpha():
            conteos[bigrama] = conteos.get(bigrama, 0) + 1
    
    total_bigramas = sum(conteos.values())
    for bigrama, recuento in conteos.items():
        conteos[bigrama] = recuento / total_bigramas
    return conteos


def calcula_distancia_media_frecuencias(freq1: dict[str, float], freq2: dict[str, float]) -> float:
    """
    Calcula la distancia media entre las frecuencias normalizadas
    representadas por dos diccionarios de frecuencias.

    Parámetros:
        freq1: Primer diccionario de frecuencias.
        freq2: Segundo diccionario de frecuencias.

    Devuelve:
        Distancia media entre los dos vectores de frecuencias, o 0.0 si ambos diccionarios están vacíos.
    """
    if len(freq1) == 0 and len(freq2) == 0:
        return 0.0
    
    todas_claves = set(freq1.keys()) | set(freq2.keys())
    suma = 0
    for bigrama in todas_claves:
        suma += abs(freq1.get(bigrama, 0) - freq2.get(bigrama, 0))
    
    return suma / len(todas_claves)  # !!!!!! => ¿puede ser 0 el denominador?


def identifica_idioma(textos_ejemplo: dict[str, str], texto_a_identificar: str) -> str:
    """
    Identifica el idioma de un texto comparando sus frecuencias de bigramas
    con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

    Parámetros:
        textos_ejemplo: Diccionario que asocia a cada idioma (por ejemplo 'es') un texto de ejemplo en ese idioma.
        texto_a_identificar: Texto cuyo idioma se quiere identificar.

    Devuelve:
        El idioma identificado del texto.
    """
    frecuencias_texto = construye_frecuencias_bigramas(texto_a_identificar)
    distancias = []
    for idioma, texto in textos_ejemplo.items():
        frecuencias_idioma = construye_frecuencias_bigramas(texto)
        d = calcula_distancia_media_frecuencias(frecuencias_texto, frecuencias_idioma)
        tupla = (d, idioma)
        distancias.append(tupla) # en realidad, se puede hacer distancias.append((d, idioma))

    return min(distancias)[1]




