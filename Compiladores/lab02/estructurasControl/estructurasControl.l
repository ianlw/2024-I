%{
#include <stdio.h>
%}

%%
si              { printf("Palabra clave: %s\n", yytext); }
mientras        { printf("Palabra clave: %s\n", yytext); }

"("             { printf("Paréntesis izquierdo: %s\n", yytext); }
")"             { printf("Paréntesis derecho: %s\n", yytext); }
"{"             { printf("Llave izquierda: %s\n", yytext); }
"}"             { printf("Llave derecha: %s\n", yytext); }

"+"             { printf("Operador de suma: %s\n", yytext); }
"-"             { printf("Operador de resta: %s\n", yytext); }
"*"             { printf("Operador de multiplicación: %s\n", yytext); }
"/"             { printf("Operador de división: %s\n", yytext); }
"=="            { printf("Operador de igualdad: %s\n", yytext); }
"!="            { printf("Operador de desigualdad: %s\n", yytext); }
"<"             { printf("Operador menor que: %s\n", yytext); }
">"             { printf("Operador mayor que: %s\n", yytext); }

[a-zA-Z]        { printf("Identificador: %s\n", yytext); }

[ \t\n]         ;
.               { printf("Error: Carácter no reconocido '%s'\n", yytext); }

%%

int yywrap() {
    return 1;
}

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
