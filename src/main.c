#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils/utils.h"

int main(int argc, char **argv) {

    Archivos *archivos = get_archivos(argv[1]);

    char output_file_path[200] = "./Entradas/";
    strcat(output_file_path, argv[1]);
    strcat(output_file_path, ".txt");

    FILE *output_file = fopen(output_file_path, "w");

    printf("sanitizando textos...\n");

    for (int i = 0; i < archivos->cantidad; i++) {

        char path[250] = "./Textos/";
        strcat(path, argv[1]);
        strcat(path, "/");
        strcat(path, archivos->nombres[i]);

        char *texto = get_texto_sanitizado(path);

        fprintf(output_file, "%s", texto);

        free(texto);

    }

    fclose(output_file);

    destruir_struct_archivos(archivos);

    printf("completando frases...\n");

    char command[100] = "python3 src/main.py ";
    strcat(command, argv[1]);

    int status = system(command);

    printf("proceso finalizado con status: %s\n", (status) ? "ERROR" : "OK");

    return 0;

}