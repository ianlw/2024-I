%

% Verificar si un número es divisible por otro
divisible(X, Y) :- 0 is X mod Y.

% Verificar si el número tiene divisores
tiene_divisores(N, D) :-
    % Verificaremos hasta la raíz cuadrada de N
    D * D =< N,        
    % Si D divide a N
    (divisible(N, D) ; 
    % Incrementar el divisor
    D1 is D + 1,       
    % Verificar de manera recursiva con el siguiente divisor
    tiene_divisores(N, D1)). 

% Verificar si un número de un dígito es primo
es_primo(N) :-
    % Verifica que sea mayor a uno y de un solo dígito
    N >= 2, N =< 9,     
    % Verifica que no tiene divisores distintos de 1 y N
    \+ tiene_divisores(N, 2). 

es_primo_un_digito(N) :-
    (es_primo(N) ->
        write(N), write(' es un número primo.');
        write(N), write(' no es un número primo.')), nl.
