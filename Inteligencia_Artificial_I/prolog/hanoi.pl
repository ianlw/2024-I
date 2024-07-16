

torres_de_hanoi(N) :-
    mover(N, 'A', 'C', 'B').

% Mover N discos desde la torre A a la torre B utilizando C como auxiliar
    % Caso base: no hay discos que mover
mover(0, _, _, _) :- !. 

mover(N, A, B, C) :-
    N > 0,
    M is N - 1,
    % Mueve M discos de A a C utilizando B como auxiliar
    mover(M, A, C, B),                  
    % Mueve el disco N de A a B
    write('Mueve el disco '), write(N), 
    write(' de '), write(A), write(' a '), write(B), nl,
    % Mueve M discos de C a B utilizando A como auxiliar
    mover(M, C, B, A).                  

