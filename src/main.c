#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils/depurador_texto.h"

int main(int argc, char **argv) {

    Archivos *archivos = get_archivos(argv[1]);

    char output_file_path[100] = "./Entradas/";
    strcat(output_file_path, argv[1]);
    strcat(output_file_path, ".txt");

    FILE *output_file = fopen(output_file_path, "w"); 

    for (int i = 0; i < archivos->cantidad; i++) {

        char path[100] = "./Textos/";
        strcat(path, argv[1]);
        strcat(path, "/");
        strcat(path, archivos->nombres[i]);

        char *texto = get_texto_sanitizado(path);

        fprintf(output_file, "%s", texto);

        free(texto);

    }

    fclose(output_file);

    destruir_struct_archivos(archivos);

    char command[50] = "python3 src/main.py ";
    strcat(command, argv[1]); 

    system(command);

    return 0;

}