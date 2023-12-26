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

def get_predicciones_derecha(palabra: str, distancia: int, map_palabras: dict, map_indices: dict, n_palabras: int) -> set:
    predicciones = set()

    for i in map_palabras[palabra]:
        if i+distancia < n_palabras:
            predicciones.add(map_indices[i+distancia])

    return predicciones     


def backward(map_palabras: dict, map_indices: dict, palabras: list, indice_predecir: int, n_palabras: int) -> set:
    predicciones = set()
    se_cumplen_condiciones = True
    i = indice_predecir
    distancia = 1

    while se_cumplen_condiciones and i > 0:

        if palabras[i-1] in map_palabras:
            pred = get_predicciones_derecha(palabras[i-1], distancia, map_palabras, map_indices, n_palabras)
        else:
            se_cumplen_condiciones = False
            
        interseccion = predicciones & pred      

        if i == indice_predecir and len(pred) == 1:
            predicciones = pred
            se_cumplen_condiciones = False
        elif i == indice_predecir and pred != set():
            predicciones = pred
        elif i == indice_predecir and pred == set():
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

a_predecir = "me hice fuerte ahi donde nunca vi nadie puede decirme quien _"

_palabras = a_predecir.split(" ")
indice_predecir = _palabras.index("_")                

print(backward(map_palabras, map_indices, _palabras, indice_predecir, n_palabras))

a_predecir = "y cuando me pierdo en la ciudad vos ya sabes comprender es solo un rato no _"

_palabras = a_predecir.split(" ")
indice_predecir = _palabras.index("_")

print(backward(map_palabras, map_indices, _palabras, indice_predecir, n_palabras))