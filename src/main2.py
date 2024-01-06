import sys

def crear_diccionario_palabras(direccion_archivo: str) -> dict:

    texto = ""
    with open(direccion_archivo, 'r') as archivo:
        texto = archivo.read()

    satinized = texto.replace("\n", " - ")

    palabras = satinized.split(" ")

    n_palabras = len(palabras)

    map_palabras = {}

    for i in range(len(palabras)):

        if palabras[i] in map_palabras:
            map_palabras.get(palabras[i]).append(i)
        else:
            map_palabras[palabras[i]] = [i]

    return map_palabras        

def predecir(map_palabras: dict, a_predecir: str) -> str:

    a_predecir = a_predecir.replace("\n", "")
    palabras = a_predecir.split(" ")
    indice_predecir = palabras.index("_")                

    return ""

def main() -> int:

    map_palabras = crear_diccionario_palabras('Entradas/' + sys.argv[1] + '.txt')

    with open('./Frases/' + sys.argv[1] + ".txt", 'r') as archivo:
        lineas = archivo.readlines()

    with open('./Salidas/' + sys.argv[1] + '.txt', 'a') as archivo:
    
        for linea in lineas:
            prediccion = predecir(map_palabras, linea)
            archivo.write(prediccion + '\n')

    

if __name__ == "__main__":
    main()             