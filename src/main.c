#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils/utils.h"

int main(int argc, char **argv) {

    Archivos *archivos = get_archivos(argv[1]);

    if (archivos == NULL || archivos->cantidad == 0) {
        printf("ERROR: Verifique que exista el directorio %s y que contenga al menos un texto\n", argv[1]);
        return 1;
    }

    char output_file_path[250] = "./Entradas/";
    strcat(output_file_path, argv[1]);
    strcat(output_file_path, ".txt");

    FILE *output_file = fopen(output_file_path, "w");

    if (output_file == NULL) {
        printf("ERROR: No se pudo crear el archivo %s\n", output_file_path);
        return 1;
    }

    printf("sanitizando textos...\n");

    for (int i = 0; i < archivos->cantidad; i++) {

        char path[300] = "./Textos/";
        strcat(path, argv[1]);
        strcat(path, "/");
        strcat(path, archivos->nombres[i]);

        char *texto = get_texto_sanitizado(path);

        if (texto == NULL) {
            printf("ERROR: No se pudo abrir el archivo de texto: %s\n", path);
            return 1;
        }

        fprintf(output_file, "%s", texto);

        free(texto);

    }

    fclose(output_file);

    destruir_struct_archivos(archivos);

    printf("completando frases...\n");

    char command[200] = "python3 src/main.py ";
    strcat(command, argv[1]);

    int status = system(command);

    printf("proceso finalizado con status: %s\n", (status) ? "ERROR" : "OK");

    return 0;

}