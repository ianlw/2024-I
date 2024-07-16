

promedio_notas :- write('Cálculo del promedio de tres notas.'), nl,
    write('Ingrese Nota1: '),
    read(Nota1), nl,
    write('Ingrese Nota2: '),
    read(Nota2), nl,
    write('Ingrese Nota3: '),
    read(Nota3), nl,
    P is (Nota1 + Nota2 + Nota3)/3,
    write('Promedio = '),
    write(P), nl.
