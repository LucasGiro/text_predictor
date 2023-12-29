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

char *get_texto_sanitizado(char *path) {

    FILE *f = fopen(path, "r");

    if (f == NULL) {
        printf("Hubo un error al abrir el archivo de texto: %s\n", path);
        return NULL;
    }

    char caracter;
    char *texto = malloc(sizeof(char) * INITIAL_BUFFER_SIZE);

    unsigned int i = 0;
    unsigned int size_texto = INITIAL_BUFFER_SIZE;

    while (fscanf(f, "%c", &caracter) != EOF) {

        if (i == size_texto) {
            size_texto += REALLOC_INCREMENT;
            texto = realloc(texto, size_texto);
        }
        if (caracter == '\n' && texto[i-1] != '\n') {
            texto [i] = ' ';
            i++;
        } else if (caracter == ' ' && texto[i-1] == '\n'){

        } else if (caracter == '.') {
            texto[i] = '\n';
            i++;
        } else if (caracter != '\n' && caracter != ',' && caracter != ';' && caracter != '?' && caracter != '!' && caracter != ':' && caracter != '-' && caracter != '(' && caracter != ')' && caracter != '¡' && caracter != '¿'){
            texto[i] = tolower(caracter);
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