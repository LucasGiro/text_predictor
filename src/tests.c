#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include "utils/utils.h"

void test_es_caracter_valido() {

    assert(es_caracter_valido('\n') == 0);
    assert(es_caracter_valido('?') == 0);
    assert(es_caracter_valido('!') == 0);
    assert(es_caracter_valido('a') == 1);
    assert(es_caracter_valido('z') == 1);
    assert(es_caracter_valido('\'') == 0);
    assert(es_caracter_valido('\"') == 0);
    assert(es_caracter_valido('-') == 0);
    assert(es_caracter_valido('_') == 0);
    assert(es_caracter_valido('b') == 1);

}

void test_get_texto_sanitizado() {

    char *path_01 = "./src/archivos_para_testing/test01.txt";
    char *result_01 = get_texto_sanitizado(path_01);
    char *path_02 = "./src/archivos_para_testing/test02.txt";
    char *result_02 = get_texto_sanitizado(path_02);
    char *path_03 = "./src/archivos_para_testing/test03.txt";
    char *result_03 = get_texto_sanitizado(path_03);

    assert(!strcmp(result_01, "esto es una prueba\nesto es una prueba\nhola mundo\nesto es un test"));
    assert(!strcmp(result_02, "y entonces y cure mis heridas\nrezo rezo rezo rezo\ny entonces\nrezo\npor vos\n"));
    assert(!strcmp(result_03, "esto es un texto para probar \nprobando el sanitizador de texto\ntesteando el sanitizador de texto \n"));
    
    free(result_01);
    free(result_02);
    free(result_03);

}

void test_get_archivos() {

    Archivos *archivos = get_archivos("Diego_Torres");
    char *nombres[] = {"cantarhastamorir.txt", "coloresperanza.txt", "guapa.txt", "quenomepierda.txt", "tratardeestarmejor.txt"};
    assert(archivos->cantidad == 5);

    for (int i = 0; i <  archivos->cantidad; i++) {
        assert(!strcmp(archivos->nombres[i], nombres[i]));
    }

    destruir_struct_archivos(archivos);


}

int main() {

    test_es_caracter_valido();

    test_get_texto_sanitizado();

    test_get_archivos();

    return 0;
}