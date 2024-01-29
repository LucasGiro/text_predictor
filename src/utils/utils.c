#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAMANO_BUFFER_INICIAL 1000
#define INCREMENTO_REALLOC 1000

typedef struct Archivos {
    int cantidad;
    char **nombres;
} Archivos;

/* es_caracter_valido: Toma un caracter y retorna 1 si es un caracter valido o 0 en caso contrario */

int es_caracter_valido(char c) {
    
    char caracteres_invalidos[] = "\n,.;?¿!¡:-()_{}[]*'/|#$\"\'\r&<> ";
    size_t longitud_caracteres_invalidos = 32;
    int es_valido = 1; 
    int i = 0;

    while (i < longitud_caracteres_invalidos && es_valido) {

        if (c == caracteres_invalidos[i]) {
            es_valido = 0;
        }

        i++;

    }

    return es_valido;
}

/* get_texto_sanitizado: Toma la ruta de un archivo de texto, sanitiza su contenido y lo almacena en memoria, retornando un puntero a dicho bloque */

char *get_texto_sanitizado(char *path) {

    FILE *f = fopen(path, "r");

    if (f == NULL) {
        printf("Hubo un error al abrir el archivo de texto: %s\n", path);
        return NULL;
    }

    char caracter;
    char ultimo_caracter = '\0';
    char *texto = malloc(sizeof(char) * TAMANO_BUFFER_INICIAL);

    unsigned int i = 0;
    unsigned int size_texto = TAMANO_BUFFER_INICIAL;

    while (fscanf(f, "%c", &caracter) != EOF) {

        if (i == size_texto) {
            size_texto += INCREMENTO_REALLOC;
            texto = realloc(texto, size_texto);
        }

        if ((caracter == '\n' || caracter == ',') && ultimo_caracter != '\n' && ultimo_caracter != ' ' && ultimo_caracter != '\0') {
            texto[i] = ' ';
            ultimo_caracter = texto[i];
            i++;
        } else if (caracter == '.' && ultimo_caracter != '\n' && ultimo_caracter != '\0') {
            texto[i] = '\n';
            ultimo_caracter = texto[i];
            i++;
        } else if ((caracter == ' ' && ultimo_caracter != '\n' && ultimo_caracter != ' ' && ultimo_caracter != '\0') || es_caracter_valido(caracter)) {
            texto[i] = tolower(caracter);
            ultimo_caracter = texto[i];
            i++;
        }
    }

    texto[i] = '\0';

    fclose(f);

    return texto;

}

/* get_archivos: Toma el nombre de un directorio dentro de Textos y retorna una estructura Archivos que contiene el nombre de todos los archivos dentro del directorio */

Archivos *get_archivos(char *folder_name) {

    char command[250] = "cd ";
    strcat(command, "./Textos/");
    strcat(command, folder_name);
    strcat(command, " && ls > ../../archivos.txt");

    system(command);

    FILE *f = fopen("./archivos.txt", "r");

    if (f == NULL) {
        printf("Hubo un error al abrir el listado de archivos textos: %s\n", "./archivos.txt");
        return NULL;
    }

    char caracter;
    Archivos *archivos = malloc(sizeof(Archivos));

    unsigned int numero_de_linea = 0;
    unsigned int i = 0;
    
    archivos->nombres = malloc(sizeof(char*));
    archivos->nombres[numero_de_linea] = malloc(sizeof(char) * 50);
    unsigned int text_size = 50;

    while (fscanf(f, "%c", &caracter) != EOF) {

        if (i == text_size) {
                text_size += sizeof(char) * 50;
                archivos->nombres[numero_de_linea] = realloc(archivos->nombres[numero_de_linea], text_size);
            }

        if (caracter != '\n') {
            archivos->nombres[numero_de_linea][i] = caracter;
            i++;
        } else {
            archivos->nombres[numero_de_linea][i] = '\0';
            i = 0;
            numero_de_linea++;
            archivos->nombres = realloc(archivos->nombres, sizeof(char*) * (numero_de_linea + 1));
            archivos->nombres[numero_de_linea] = malloc(sizeof(char) * 50); // cuando se llegue a EOF, esta asignacion hara que sobre un bloque de memoria
        }

    }

    archivos->cantidad = numero_de_linea;
    free(archivos->nombres[numero_de_linea]); // liberando el bloque de memoria que sobra

    fclose(f);

    return archivos;

}

// destruir_struct_archivos: Recibe un puntero a una estructura Archivos y libera la memoria ocupada por esa estructura

void destruir_struct_archivos(Archivos *archivos) {

    for (int i = 0; i < archivos->cantidad; i++) {
        free(archivos->nombres[i]);
    }

    if (archivos->cantidad > 0) {
        free(archivos->nombres);
    }

    free(archivos);

}