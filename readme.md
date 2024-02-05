# Compilación del Proyecto

Para compilar el programa escrito en C, correr:
```bash
gcc ./src/utils/utils.c ./src/main.c -o main
```

Para compilar el archivo de tests de C, correr:
```bash
gcc ./src/utils/utils.c ./src/tests.c -o tests
```

# Testing

Una vez compilado el archivo de tests de C, ejecutar el archivo `./tests` para correr los tests de C.

Para los tests de python, correr: `python3 -m pytest src/tests.py`.

# Descripción General del Proyecto

## Python

### Estructuras de Datos Utilizadas

- **palabras_texto:** Lista que almacenará las palabras del texto sanitizado, donde el string "-" marca la separación entre las oraciones. En otras palabras, es el texto sanitizado representado en forma de lista, donde cada posición es una palabra, y "-" representa la separación entre las oraciones.
- **indices_palabras:** Es un diccionario que tiene como clave una palabra del texto sanitizado, en la cual se almacenará como valor una lista de índices donde se encuentra esa palabra en palabras_texto.
- **apariciones:** Es un diccionario que tiene como clave una palabra del texto sanitizado, donde el valor será un entero que indique la cantidad de veces que apareció esa palabra durante el proceso de predicción de una frase.
- **predicciones:** Conjunto donde se irán almacenando las posibles predicciones para una frase.

**Elegí este conjunto de estructuras ya que fue el más optimizado (el que menos memoria usó) de todas las demás opciones que probé y además por la simpleza de resolución que ofrecían para el problema.**

### Solución Propuesta

La solución consiste en una serie de pasos ordenados. A modo de resumen y omitiendo algunos detalles, ésto es lo que hace el algoritmo: (como ejemplo tomamos la frase "esto es _ ejemplo")

1. El programa comienza analizando las palabras que están detrás de la palabra a predecir, en este caso, toma la palabra "es" y busca en indices_palabras en qué índices de palabras_texto se encuentra dicha palabra.
2. A cada índice le suma 1 (la distancia a la que esta "es" de la palabra a predecir) y busca esos índices en palabras_texto, obteniendo así, posibles palabras para completar, las cuales se almacenarán en predicciones y apariciones.
3. Luego se hace lo mismo con la palabra "esto", pero ahora tomando distancia = 2 y analizando si entre medio de dicha palabra y la posible a predecir no se encuentra un "-", ya que si esto sucede, la palabra predecida estaría en otra oración. Luego interseco este conjunto de nuevas palabras con el conjunto predicciones. Si la intersección es vacía, entonces se queda con las predicciones hechas anteriormente y deja de buscar.
4. Si el número de predicciones al intersecar es mayor que 1 y ya no hay más palabras para analizar, entonces realiza el mísmo procedimiento pero con las palabras que están adelante de la palabra a predecir (ahora a los indices se les resta la distancia), pero trabajando con el conjunto de predicciones ya obtenido anteriormente, siendo éste de mayor importancia que las posibles nuevas predicciones. Ahora el objetivo es achicar lo más posible el conjunto predicciones haciendo intersección con las nuevas palabras predecidas.
5. Una vez terminada la búsqueda y teniendo el conjunto de predicciones, utilizo el diccionario de apariciones y elijo la palabra con mayor número de apariciones y que además esté en el conjunto predicciones. Si en el paso 3 o 4 la intersección de las predicciones es exactamente 1, el algoritmo deja de buscar y declara esa única predicción como la definitiva.

### Caso Especial

Si no se logra encontrar ninguna predicción a partir de las palabras anteriores, entonces se procede con el paso 4 con un conjunto predicciones vacío y una busqueda similar a la mencionada anteriormente.

**Observación**: como se puede notar, se les está dando mayor importancia a las predicciones obtenidas de palabras anteriores a la que se tiene que predecir. Esa fue una decisión importante, pues si fuera otro el orden de importancia, el algoritmo estaría dando resultados diferentes. Tomé esta decisión ya que fue la que mejores resultados de predicción me dió comparado a otras (como por ejemplo que no haya un orden de importancia).

## C

### Estructuras de Datos Utilizadas

- **Archivos:** Struct que almacena la cantidad de archivos que tiene un directorio y un array de strings con sus nombres.

### Solución Propuesta para Leer y Sanitizar los Textos

Por cada archivo .txt que lee el programa, éste guarda su contenido sanitizado en memoria y luego lo vuelca en el archivo de salida .txt. Para esto, usé memoria dinámica, pidiendo al sistema operativo a medida que el programa necesitara más para poder seguir almacenando el texto. 

Usé este enfoque ya que permite manejar archivos de tamaño aleatorio y muy grandes, a la vez que utiliza solo la cantidad de memoria necesaria (puede sobrar un poco, pero es una cantidad muy pequeña).
Además, volcar todo el texto sanitizado de una sola vez realiza menos llamadas de escritura al disco del equipo, haciendo que este enfoce sea más rápido que ir leyendo y escribiendo al mismo tiempo.

**Estudiante: Lucas Giro**