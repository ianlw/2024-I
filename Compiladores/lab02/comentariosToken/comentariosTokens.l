%{
#include <stdio.h>
%}

%option noyywrap

/* Define el nombre del archivo */

%%

"//"(.*)       { /* Comentario de una línea */
                    printf("Comentario: %s\n", yytext + 2); // El comentario comienza después de los primeros dos caracteres "//"
                 }

"/*"            { /* Comentario multilinea */
                    printf("Comentario multilinea: ");
                    int comentario_abierto = 1;
                    while (comentario_abierto) {
                        char c = input();
                        if (c == '*') {
                            c = input();
                            if (c == '/') {
                                comentario_abierto = 0;
                            }
                        } else {
                            putchar(c);
                        }
                    }
                    printf("\n");
                 }

inicio          { printf("Palabra clave: inicio\n"); }
fin             { printf("Palabra clave: fin\n"); }
si              { printf("Palabra clave: si\n"); }
sino            { printf("Palabra clave: sino\n"); }

.               { /* Ignorar caracteres desconocidos */ }

%%

int main() {
    #define ARCHIVO_CODIGO "codigo.a"
    FILE *archivo = fopen(ARCHIVO_CODIGO, "r");
    if (archivo == NULL) {
        fprintf(stderr, "Error al abrir el archivo %s\n", ARCHIVO_CODIGO);
        return -1;
    }

    yyin = archivo; // Establecer el archivo de entrada para Lex

    yylex();

    fclose(archivo);
    return 0;
}
