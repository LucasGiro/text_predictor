typedef struct Archivos {
    int cantidad;
    char **nombres;
} Archivos;

char *depurar_texto_archivo(char *path);

Archivos *get_archivos(char *nombre_carpeta);