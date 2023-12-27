#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv) {

    FILE *f = fopen("../Textos/Luis_Spinetta/Rezo_por_vos.txt", "r");
    char caracter;
    char texto[5000];

    int i = 0;

    while (fscanf(f, "%c", &caracter) != EOF) {
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

    printf("%s", texto);

    return 0;

}