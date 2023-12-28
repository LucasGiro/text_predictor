#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils/depurador_texto.h"

int main(int argc, char **argv) {

    Archivos *archivos = get_archivos("Diego_Torres");

    destruir_struct_archivos(archivos);

    /*char path[] = "./Textos/Diego_Torres/quenomepierda.txt";

    char *texto = get_texto_sanitizado(path);

    long int index = strlen(texto);

    printf("%s", texto);

    free(texto);*/

    return 0;

}