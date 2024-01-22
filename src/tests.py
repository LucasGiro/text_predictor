from main import palabra_con_mas_apariciones, backward, es_prediccion_derecha_valida, es_prediccion_izquierda_valida, forward, get_predicciones_derecha, get_predicciones_izquierda, predecir

def test_palabra_con_mas_apariciones():

    apariciones = { 'programa': 4, 'python': 1, 'aplicacion': 2, 'sistema':3 }
    predicciones = set()
    predicciones.update(['programa', 'sistema'])

    assert palabra_con_mas_apariciones(apariciones, predicciones) == 'programa'

def test_es_prediccion_derecha_valida():
    indice_palabra_base = 2
    indice_palabra_predecida = 6
    map_indices = { 0: 'esto', 1: 'es', 2: 'un', 3: 'caso', 4: 'de', 5: 'test', 6: 'en', 7:'python' }

    assert es_prediccion_derecha_valida(indice_palabra_base, indice_palabra_predecida, map_indices) == True

    indice_palabra_base = 0
    indice_palabra_predecida = 3
    map_indices = { 0: 'hola', 1: 'mundo', 2: '-', 3: 'esto', 4: 'es', 5: 'un', 6: 'test' }

    assert es_prediccion_derecha_valida(indice_palabra_base, indice_palabra_predecida, map_indices) == False

def test_es_prediccion_izquierda_valida():
    indice_palabra_base = 6
    indice_palabra_predecida = 2
    map_indices = { 0: 'esto', 1: 'es', 2: 'un', 3: 'caso', 4: 'de', 5: 'test', 6: 'en', 7:'python' }

    assert es_prediccion_izquierda_valida(indice_palabra_base, indice_palabra_predecida, map_indices) == True

    indice_palabra_base = 3
    indice_palabra_predecida = 0
    map_indices = { 0: 'hola', 1: 'mundo', 2: '-', 3: 'esto', 4: 'es', 5: 'un', 6: 'test' }

    assert es_prediccion_izquierda_valida(indice_palabra_base, indice_palabra_predecida, map_indices) == False

def test_get_predicciones_derecha():
    ## "hoy haremos los casos de test en python manana haremos los de c"
    ## haremos los casos de _
    palabra = 'casos'
    distancia = 2
    map_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    map_indices = { 0: 'hoy', 1: 'haremos', 2: 'los', 3: 'casos', 4: 'de', 5: 'test', 6: 'en', 7: 'python', 8: 'manana', 9: 'haremos', 10: 'los', 11: 'de', 12: 'c' }
    n_palabras = 13
    apariciones = {}

    assert get_predicciones_derecha(palabra, distancia, map_palabras, map_indices, n_palabras, apariciones) == { 'test' }

def test_get_predicciones_izquierda():
    ## "hoy haremos los casos de test en python manana haremos los de c"
    ## _ los casos
    palabra = 'casos'
    distancia = 2
    map_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    map_indices = { 0: 'hoy', 1: 'haremos', 2: 'los', 3: 'casos', 4: 'de', 5: 'test', 6: 'en', 7: 'python', 8: 'manana', 9: 'haremos', 10: 'los', 11: 'de', 12: 'c' }
    apariciones = {}

    assert get_predicciones_izquierda(palabra, distancia, map_palabras, map_indices, apariciones) == { 'haremos' }

def test_backward():
    palabras = ['_', 'los', 'casos']
    indice_predecir = 0
    n_palabras = 13
    apariciones = {}
    map_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    map_indices = { 0: 'hoy', 1: 'haremos', 2: 'los', 3: 'casos', 4: 'de', 5: 'test', 6: 'en', 7: 'python', 8: 'manana', 9: 'haremos', 10: 'los', 11: 'de', 12: 'c' }

    assert backward(map_palabras, map_indices, palabras, indice_predecir, n_palabras, apariciones) == set()

    palabras = ['haremos', 'los', 'casos', 'de', '_']
    indice_predecir = 4

    assert backward(map_palabras, map_indices, palabras, indice_predecir, n_palabras, apariciones) == { 'test' }

def test_forward():
    palabras = ['_', 'los', 'casos']
    indice_predecir = 0
    apariciones = {}
    map_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    map_indices = { 0: 'hoy', 1: 'haremos', 2: 'los', 3: 'casos', 4: 'de', 5: 'test', 6: 'en', 7: 'python', 8: 'manana', 9: 'haremos', 10: 'los', 11: 'de', 12: 'c' }
    predicciones = set()

    assert forward(map_palabras, map_indices, palabras, indice_predecir, predicciones, apariciones) == { 'haremos' }

    palabras = ['haremos', 'los', 'casos', 'de', '_']
    indice_predecir = 4

    assert forward(map_palabras, map_indices, palabras, indice_predecir, predicciones ,apariciones) == set()


def test_predecir():
    map_palabras = { 'hoy': [0], 'haremos': [1, 9], 'los': [2, 10], 'casos': [3], 'de': [4, 11], 'test': [5], 'en': [6], 'python': [7], 'manana': [8], 'c': [12] }
    map_indices = { 0: 'hoy', 1: 'haremos', 2: 'los', 3: 'casos', 4: 'de', 5: 'test', 6: 'en', 7: 'python', 8: 'manana', 9: 'haremos', 10: 'los', 11: 'de', 12: 'c' }
    n_palabras = 13
    frase_a_predecir = "haremos los casos de _"

    assert predecir(map_palabras, map_indices, frase_a_predecir, n_palabras) == "haremos los casos de test"