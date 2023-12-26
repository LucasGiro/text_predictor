texto = "el amor despues del amor tal vez se parezca a este rayo de sol\ny ahora que busque y ahora que encontre el perfume que lleva el dolor\nen la esencia de las almas en la ausencia del dolor\nahora se que ya no puedo vivir sin tu amor\nme hice fuerte ahi donde nunca vi nadie puede decirme quien soy\nyo lo se muy bien que aprendi a querer el perfume que lleva el dolor\nen la esencia de las almas dice toda religion para mi que es el amor despues del amor\nte vi juntabas margaritas del mantel\nya se que te trate bastante mal\nno se si eras un angel o un rubi o simplemente te vi\nte vi saliste entre la gente a saludar\nlos astros se rieron otra vez\nla llave de mandala se quebro o simplemente te vi\ntodo lo que diga esta de mas las luces siempre encienden en el alma\ny cuando me pierdo en la ciudad vos ya sabes comprender es solo un rato no mas\ntendria que llorar o salir a matar\nte vi te vi te vi\nyo no buscaba nadie y te vi"

satinized = texto.replace("\n", " - ")

palabras = satinized.split(" ")

n_palabras = len(palabras)

map_palabras = {}
map_indices = {}

for i in range(len(palabras)):
    map_indices[i] = palabras[i]

    if palabras[i] in map_palabras:
        map_palabras.get(palabras[i]).append(i)
    else:
        map_palabras[palabras[i]] = [i] 

##Primera etapa
        
def es_prediccion_derecha_valida(indice_palabra_base: int, indice_palabra_predecida: int, map_indices: dict) -> bool:
    
    i = indice_palabra_base + 1
    es_valida = True

    while i <= indice_palabra_predecida and es_valida:
        if map_indices[i] == "-": ## tambien funciona haciendo que si la palabra predecida es - entonces dicha palabra no es valida
            es_valida = False
        i += 1

    return es_valida        


def get_predicciones_derecha(palabra: str, distancia: int, map_palabras: dict, map_indices: dict, n_palabras: int) -> set:
    predicciones = set()

    for i in map_palabras[palabra]:
        if (i+distancia) < n_palabras and es_prediccion_derecha_valida(i, i+distancia, map_indices):
            predicciones.add(map_indices[i+distancia])

    return predicciones     


def backward(map_palabras: dict, map_indices: dict, palabras: list, indice_predecir: int, n_palabras: int) -> set:
    predicciones = set()
    se_cumplen_condiciones = True
    i = indice_predecir
    distancia = 1

    while se_cumplen_condiciones and i > 0:

        pre_predicciones = set()

        if palabras[i-1] in map_palabras:
            pre_predicciones = get_predicciones_derecha(palabras[i-1], distancia, map_palabras, map_indices, n_palabras)
        else:
            se_cumplen_condiciones = False
            
        interseccion = predicciones & pre_predicciones      

        if i == indice_predecir and len(pre_predicciones) == 1:
            predicciones = pre_predicciones
            se_cumplen_condiciones = False
        elif i == indice_predecir and pre_predicciones != set():
            predicciones = pre_predicciones
        elif i == indice_predecir and pre_predicciones == set():
            se_cumplen_condiciones = False
        elif (interseccion) == set() and i != indice_predecir:
            se_cumplen_condiciones = False
        elif len((interseccion)) == 1:
            predicciones = interseccion
            se_cumplen_condiciones = False    
        else:
            predicciones = interseccion      

        distancia += 1
        i -= 1

    return predicciones

a_predecir = "el amor antes del amor capaz se parezca a este rayo de _"

_palabras = a_predecir.split(" ")
indice_predecir = _palabras.index("_")                

print(backward(map_palabras, map_indices, _palabras, indice_predecir, n_palabras))

a_predecir = "y cuando me pierdo en la ciudad vos ya sabes comprender es solo un rato no _"

_palabras = a_predecir.split(" ")
indice_predecir = _palabras.index("_")

print(backward(map_palabras, map_indices, _palabras, indice_predecir, n_palabras))