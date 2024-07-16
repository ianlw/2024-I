

/* Calcular el promedio de tres notas */

leer_notas(N1, N2, N3):-
    write('Ingrese nota 1: '),
    read(N1), nl,
    write('Ingrese nota 2: '),
    read(N2), nl,
    write('Ingrese nota 3: '),
    read(N3), nl.

calcular_promedio(N1, N2, N3, P) :- P is (N1+N2+N3)/3.

mostrar_promedio(P) :-
    write('Promedio = '),
    write(P), nl.

mensaje(P, M) :- P >= 13.5, M = aprobado.
mensaje(P, M) :- P >= 8.5, P < 13.5, M = desaprobado.
mensaje(P, M) :- P < 8.5, M = reprobado.

mostrar_mensaje(P) :-
    mensaje(P, M),
    write(M), nl.

promedio_nota :-
    leer_notas(N1, N2, N3),
    calcular_promedio(N1, N2, N3, P),
    mostrar_promedio(P),
    mostrar_mensaje(P).
