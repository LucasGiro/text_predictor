#include <stdio.h>
#include <assert.h>
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

int main() {

    test_es_caracter_valido();

    return 0;
}