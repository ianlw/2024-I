
distancia_dos_puntos :- write('Calculo de la distancia dos puntos.'), nl,
    write('Ingrese el punto x1: '),
    read(X1), nl,
    write('Ingrese el punto y1: '),
    read(Y1), nl,
    write('Ingrese el punto x2: '),
    read(X2), nl,
    write('Ingrese el punto y2: '),
    read(Y2), nl,
    DistanciaX is X2 - X1,
    DistanciaY is Y2 - Y1,
    Distancia is sqrt(DistanciaX * DistanciaX + DistanciaY * DistanciaY), nl,
    write('La distancia entre los puntos es: '),
    write(Distancia), nl.
