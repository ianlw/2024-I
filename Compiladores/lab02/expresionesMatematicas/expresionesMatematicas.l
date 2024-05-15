%{
#include <stdio.h>
%}

%%

"+"             { printf("Operador de suma: %s\n", yytext); }
"-"             { printf("Operador de resta: %s\n", yytext); }
"*"             { printf("Operador de multiplicación: %s\n", yytext); }
"/"             { printf("Operador de división: %s\n", yytext); }
"^"             { printf("Operador de potencia: %s\n", yytext); }

"("             { printf("Paréntesis izquierdo: %s\n", yytext); }
")"             { printf("Paréntesis derecho: %s\n", yytext); }

[0-9]+(\.[0-9]+)?   { printf("Número: %s\n", yytext); }
[ \t\n]         ;   // Ignorar espacios en blanco y nuevas líneas
.               { printf("Error: Carácter no reconocido '%s'\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    #define ARCHIVO_CODIGO "expresiones.txt"
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

