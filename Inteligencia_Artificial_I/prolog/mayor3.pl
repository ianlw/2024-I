

/*Programa para calcular el mayor de tres números */

leer_nros(N1, N2, N3) :-
    write('Ingrese nro 1: '),
    read(N1), nl,
    write('Ingrese nro 2: '),
    read(N2), nl,
    write('Ingrese nro 3: '),
    read(N3), nl.

mayor_tres(N1, N2, N3, M) :-
    (N1 >= N2, N1 >= N2, M = N1);
    (N2 >= N1, N2 >= N3, M = N2);
    (N3 >= N1, N3 >= N2, M = N3).

mostrar_mayor(M) :-
    write('Mayor = '), write(M), nl.

mayor :-
    leer_nros(N1, N2, N3),
    mayor_tres(N1, N2, N3, M),
    mostrar_mayor(M).


