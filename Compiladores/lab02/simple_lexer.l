%{
#include <stdio.h>
%}

%option noyywrap

%%
[ \t]+ ; /* Ignorar espacios en blanco */
[a-zA-Z][a-zA-Z0-9]* { printf("IDENTIFICADOR: %s\n", yytext); }
[0-9]+ { printf("NUMERO: %s\n", yytext); }
"+" { printf("OPERADOR SUMA: %s\n", yytext); }
"-" { printf("OPERADOR RESTA: %s\n", yytext); }
. { printf("CARACTER NO RECONOCIDO: %s\n", yytext); }
%%
int main() {
printf("Ingrese el código a analizar:\n");
yylex();
return 0;
}
