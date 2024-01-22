typedef struct Archivos {
    int cantidad;
    char **nombres;
} Archivos;

int es_caracter_valido(char c);

char *get_texto_sanitizado(char *path);
 
Archivos *get_archivos(char *nombre_carpeta);

void destruir_struct_archivos(Archivos *archivos);