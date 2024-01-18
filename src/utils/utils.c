#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_BUFFER_SIZE 1000
#define REALLOC_INCREMENT 1000

typedef struct Archivos {
    int cantidad;
    char **nombres;
} Archivos;

int es_caracter_valido(char c) {
    
    char caracteres_invalidos[] = "\n,.;?¿!¡:-()_{}[]*'/|#$\"\'\r& ";
    size_t longitud_caracteres_invalidos = strlen(caracteres_invalidos);
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

char *get_texto_sanitizado(char *path) {

    FILE *f = fopen(path, "r");

    if (f == NULL) {
        printf("Hubo un error al abrir el archivo de texto: %s\n", path);
        return NULL;
    }

    char caracter;
    char ultimo_caracter = '\0';
    char *texto = malloc(sizeof(char) * INITIAL_BUFFER_SIZE);

    unsigned int i = 0;
    unsigned int size_texto = INITIAL_BUFFER_SIZE;

    while (fscanf(f, "%c", &caracter) != EOF) {

        if (i == size_texto) {
            size_texto += REALLOC_INCREMENT;
            texto = realloc(texto, size_texto);
        }
        if ((caracter == '\n' || caracter == ',') && ultimo_caracter != '\n' && ultimo_caracter != ' ') {
            texto[i] = ' ';
            ultimo_caracter = texto[i];
            i++;
        } else if (caracter == '.' && ultimo_caracter != '\n') {
            texto[i] = '\n';
            ultimo_caracter = texto[i];
            i++;
        } else if ((caracter == ' ' && ultimo_caracter != '\n' && ultimo_caracter != ' ') || es_caracter_valido(caracter)) {
            texto[i] = tolower(caracter);
            ultimo_caracter = texto[i];
            i++;
        }
    }

    texto[i] = '\0';

    fclose(f);

    return texto;

}

Archivos *get_archivos(char *folder_name) {

    char command[100] = "cd ";
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
            archivos->nombres[numero_de_linea] = malloc(sizeof(char) * 50);
        }

    }

    archivos->cantidad = numero_de_linea;

    fclose(f);

    return archivos;

}

void destruir_struct_archivos(Archivos *archivos) {

    for (int i = 0; i < archivos->cantidad; i++) {
        free(archivos->nombres[i]);
    }

    free(archivos->nombres);
    free(archivos);

}