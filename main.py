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


a_predecir = "y ahora que _ y ahora que"

_palabras = a_predecir.split(" ")
indice_predecir = _palabras.index("_")

##Primera etapa

predicciones = set()
se_cumplen_condiciones = True
i = indice_predecir
contador = 1
while se_cumplen_condiciones and i >= 3:

    if _palabras[i-1] in map_palabras and _palabras[i-1] != "-":
        pred = set()
        for p in map_palabras[_palabras[i-1]]:
            pred.add(map_indices[p+contador])   

    if contador > 1 and (predicciones & pred) == set():
        se_cumplen_condiciones = False
    elif contador > 1:
        predicciones.intersection(pred) 
    else:
        predicciones.update(pred)    

    contador += 1
    i -= 1             

print(predicciones)