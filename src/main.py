import sys
def palabra_con_mas_apariciones(apariciones: dict, predicciones: set) -> str:

    resultado = ("", 0)

    for p in apariciones:
        if apariciones[p] > resultado[1] and p in predicciones:
            resultado = (p, apariciones[p])

    return resultado[0]

        
def es_prediccion_derecha_valida(indice_palabra_base: int, indice_palabra_predecida: int, palabras_texto: list[str]) -> bool:
    
    i = indice_palabra_base + 1
    es_valida = True

    while i <= indice_palabra_predecida and es_valida:
        if palabras_texto[i] == "-": ## tambien funciona haciendo que si la palabra predecida es - entonces dicha palabra no es valida
            es_valida = False
        i += 1

    return es_valida

def es_prediccion_izquierda_valida(indice_palabra_base: int, indice_palabra_predecida: int, palabras_texto: list[str]) -> bool:
    i = indice_palabra_base - 1
    es_valida = True

    while i >= indice_palabra_predecida and es_valida:
        if palabras_texto[i] == "-": ## tambien funciona haciendo que si la palabra predecida es - entonces dicha palabra no es valida
            es_valida = False
        i -= 1

    return es_valida


def get_predicciones_derecha(palabra: str, distancia: int, map_palabras: dict, palabras_texto: list[str], n_palabras: int, apariciones: dict) -> set:
    predicciones = set()

    for i in map_palabras[palabra]:
        if (i+distancia) < n_palabras and es_prediccion_derecha_valida(i, i+distancia, palabras_texto):
            predicciones.add(palabras_texto[i+distancia])
            if palabras_texto[i+distancia] in apariciones:
                apariciones[palabras_texto[i+distancia]] += 1
            else:
                apariciones[palabras_texto[i+distancia]] = 1    

    return predicciones

def get_predicciones_izquierda(palabra: str, distancia: int, map_palabras: dict, palabras_texto: list[str], apariciones: dict) -> set:
    predicciones = set()

    for i in map_palabras[palabra]:
        if (i-distancia) >= 0 and es_prediccion_izquierda_valida(i, i-distancia, palabras_texto):
            predicciones.add(palabras_texto[i-distancia])
            if palabras_texto[i-distancia] in apariciones:
                apariciones[palabras_texto[i-distancia]] += 1
            else:
                apariciones[palabras_texto[i-distancia]] = 1

    return predicciones


def backward(map_palabras: dict, palabras_texto: list[str], palabras_frase: list[str], indice_predecir: int, n_palabras: int, apariciones: dict) -> set:
    predicciones = set()
    continuar_busqueda = True
    i = indice_predecir
    distancia = 1

    while continuar_busqueda and i > 0:

        nuevas_predicciones = set()

        if palabras_frase[i-1] in map_palabras:
            nuevas_predicciones = get_predicciones_derecha(palabras_frase[i-1], distancia, map_palabras, palabras_texto, n_palabras, apariciones)
            
            if predicciones == set():
                predicciones = nuevas_predicciones

            interseccion = predicciones & nuevas_predicciones      

            if len(interseccion) == 1:
                predicciones = interseccion
                continuar_busqueda = False
            elif interseccion != set():
                predicciones = interseccion
            else:
                continuar_busqueda = False

        distancia += 1
        i -= 1

    return predicciones

def forward(map_palabras: dict, palabras_texto: list[str], palabras_frase: list[str], indice_predecir: int, predicciones: set, apariciones: dict) -> set:
    continuar_busqueda = True
    i = indice_predecir
    distancia = 1

    while continuar_busqueda and i < (len(palabras_frase) - 1):

        nuevas_predicciones = set()

        if palabras_frase[i+1] in map_palabras:
            nuevas_predicciones = get_predicciones_izquierda(palabras_frase[i+1], distancia, map_palabras, palabras_texto, apariciones)
            
            if predicciones == set():
                predicciones = nuevas_predicciones 

            interseccion = predicciones & nuevas_predicciones     

            if len(interseccion) == 1:
                predicciones = interseccion
                continuar_busqueda = False    
            elif interseccion != set():
                predicciones = interseccion
              
        distancia += 1
        i += 1

    return predicciones

def predecir(map_palabras: dict, palabras_texto: list[str], frase_a_predecir: str, n_palabras: int) -> str:

    frase_a_predecir = frase_a_predecir.replace("\n", "")
    palabras_frase = frase_a_predecir.split(" ")
    indice_predecir = palabras_frase.index("_")                

    apariciones = dict()

    # busco entre las palabras que estan antes de la que tengo que predecir
    predicciones = backward(map_palabras, palabras_texto, palabras_frase, indice_predecir, n_palabras, apariciones)
    # busco entre las palabras que estan despues de la que tengo que predecir
    predicciones = forward(map_palabras, palabras_texto, palabras_frase, indice_predecir, predicciones, apariciones)

    # busco la palabra que mas apariciones tuvo durante el proceso de prediccion y que además este en el conjunto predicciones, luego reemplazo el guion bajo con esa palabra
    return frase_a_predecir.replace("_", palabra_con_mas_apariciones(apariciones, predicciones))

def main() -> None:

    texto_sanitizado = ""

    entrada = open('./Entradas/' + sys.argv[1] + '.txt', 'r')
    texto_sanitizado = entrada.read()
    entrada.close()

    texto_sanitizado = texto_sanitizado.replace("\n", " - ")

    palabras_texto = texto_sanitizado.split(" ")

    n_palabras = len(palabras_texto)

    map_palabras = {} # almacena en cada key la palabra y como valor una lista de indices donde aparece la palabra

    for i in range(n_palabras):

        if palabras_texto[i] in map_palabras:
            map_palabras.get(palabras_texto[i]).append(i)
        else:
            map_palabras[palabras_texto[i]] = [i]

    archivo_frases = open('./Frases/' + sys.argv[1] + ".txt", 'r')
    frases = archivo_frases.readlines()
    archivo_frases.close()

    archivo_salida = open('./Salidas/' + sys.argv[1] + '.txt', 'a')
    
    for frase in frases:
        prediccion = predecir(map_palabras, palabras_texto, frase, n_palabras)
        archivo_salida.write(prediccion + '\n')

    archivo_salida.close()


if __name__ == "__main__":
    main()
