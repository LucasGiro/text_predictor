#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils/depurador_texto.h"

int main(int argc, char **argv) {

    get_archivos("");

    char path[] = "./Textos/Diego_Torres/quenomepierda.txt";

    char *texto = depurar_texto_archivo(path);

    long int index = strlen(texto);

    printf("%s", texto);

    free(texto);

    return 0;

}