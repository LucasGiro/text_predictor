#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *depurar_texto_archivo(char *path) {

    FILE *f = fopen(path, "r");

    if (f == NULL) {
        printf("Hubo un error al abrir el archivo de texto: %s\n", path);
        return NULL;
    }

    char caracter;
    char *texto = malloc(sizeof(char) * 500);

    int i = 0;
    int reallocs = 1;

    while (fscanf(f, "%c", &caracter) != EOF) {

        if ((i / reallocs) > 499) {
            reallocs++;
            texto = realloc(texto, 500*reallocs);
        }
        if (caracter == '\n' && texto[i-1] != '\n') {
            texto [i] = ' ';
            i++;
        } else if (caracter == ' ' && texto[i-1] == '\n'){

        } else if (caracter == '.') {
            texto[i] = '\n';
            i++;
        } else if (caracter != '\n' && caracter != ',' && caracter != ';' && caracter != '?' && caracter != '!'){
            texto[i] = tolower(caracter);
            i++;
        }
    }

    texto[i] = '\0';

    fclose(f);

    return texto;

}