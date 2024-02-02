from main import palabra_con_mas_apariciones, backward, es_prediccion_derecha_valida, es_prediccion_izquierda_valida, forward, get_predicciones_derecha, get_predicciones_izquierda, predecir

def test_palabra_con_mas_apariciones():

    apariciones = { 'programa': 4, 'python': 1, 'aplicacion': 2, 'sistema':3 }
    predicciones = set()
    predicciones.update(['programa', 'sistema'])

    assert palabra_con_mas_apariciones(apariciones, predicciones) == 'programa'

def test_es_prediccion_derecha_valida():
    indice_palabra_base = 2
    indice_palabra_predecida = 6
    palabras_texto = ['esto', 'es', 'un', 'caso', 'de', 'test', 'en', 'python']

    assert es_prediccion_derecha_valida(indice_palabra_base, indice_palabra_predecida, palabras_texto) == True

    indice_palabra_base = 0
    indice_palabra_predecida = 3
    palabras_texto = ['hola', 'mundo', '-', 'esto', 'es', 'un', 'test']

    assert es_prediccion_derecha_valida(indice_palabra_base, indice_palabra_predecida, palabras_texto) == False

def test_es_prediccion_izquierda_valida():
    indice_palabra_base = 6
    indice_palabra_predecida = 2
    palabras_texto = ['esto', 'es', 'un', 'caso', 'de', 'test', 'en', 'python']

    assert es_prediccion_izquierda_valida(indice_palabra_base, indice_palabra_predecida, palabras_texto) == True

    indice_palabra_base = 3
    indice_palabra_predecida = 0
    palabras_texto = ['hola', 'mundo', '-', 'esto', 'es', 'un', 'test']

    assert es_prediccion_izquierda_valida(indice_palabra_base, indice_palabra_predecida, palabras_texto) == False

def test_get_predicciones_derecha():
    ## texto: "hoy haremos los casos de test en python manana haremos los de c"
    ## frase a predecir: haremos los casos de _
    palabra = 'casos'
    distancia = 2
    indices_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    palabras_texto = ['hoy', 'haremos', 'los', 'casos', 'de', 'test', 'en', 'python', 'manana', 'haremos', 'los', 'de', 'c']
    n_palabras = 13
    apariciones = {}

    assert get_predicciones_derecha(palabra, distancia, indices_palabras, palabras_texto, n_palabras, apariciones) == { 'test' }
    assert apariciones['test'] == 1

def test_get_predicciones_izquierda():
    ## "hoy haremos los casos de test en python manana haremos los de c"
    ## _ haremos los casos
    palabra = 'haremos'
    distancia = 1
    indices_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    palabras_texto = ['hoy', 'haremos', 'los', 'casos', 'de', 'test', 'en', 'python', 'manana', 'haremos', 'los', 'de', 'c']
    apariciones = {}

    assert get_predicciones_izquierda(palabra, distancia, indices_palabras, palabras_texto, apariciones) == { 'hoy', 'manana' }
    assert apariciones['hoy'] == 1
    assert apariciones['manana'] == 1

def test_backward():
    palabras = ['_', 'los', 'casos']
    indice_predecir = 0
    n_palabras = 13
    apariciones = {}
    indices_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    palabras_texto = ['hoy', 'haremos', 'los', 'casos', 'de', 'test', 'en', 'python', 'manana', 'haremos', 'los', 'de', 'c']

    assert backward(indices_palabras, palabras_texto, palabras, indice_predecir, n_palabras, apariciones) == set()

    palabras = ['haremos', 'los', 'casos', 'de', '_']
    indice_predecir = 4

    assert backward(indices_palabras, palabras_texto, palabras, indice_predecir, n_palabras, apariciones) == { 'test' }

    palabras = ['hoy', 'haremos', '_', 'de']
    indice_predecir = 2

    assert backward(indices_palabras, palabras_texto, palabras, indice_predecir, n_palabras, apariciones) == { 'los' }

def test_forward():
    palabras = ['_', 'los', 'casos']
    indice_predecir = 0
    apariciones = {}
    indices_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    palabras_texto = ['hoy', 'haremos', 'los', 'casos', 'de', 'test', 'en', 'python', 'manana', 'haremos', 'los', 'de', 'c']
    predicciones = set()

    assert forward(indices_palabras, palabras_texto, palabras, indice_predecir, predicciones, apariciones) == { 'haremos' }

    palabras = ['haremos', 'los', 'casos', 'de', '_']
    indice_predecir = 4

    assert forward(indices_palabras, palabras_texto, palabras, indice_predecir, predicciones ,apariciones) == set()

    palabras = ['_', 'haremos', 'los']
    indice_predecir = 0

    assert forward(indices_palabras, palabras_texto, palabras, indice_predecir, predicciones ,apariciones) == { 'hoy', 'manana' }


def test_predecir():
    indices_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    palabras_texto = ['hoy', 'haremos', 'los', 'casos', 'de', 'test', 'en', 'python', 'manana', 'haremos', 'los', 'de', 'c']
    n_palabras = 13
    frase_a_predecir = "haremos los casos de _"

    assert predecir(indices_palabras, palabras_texto, frase_a_predecir, n_palabras) == "haremos los casos de test"