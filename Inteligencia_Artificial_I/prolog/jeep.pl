

% Predicado principal para calcular la distancia máxima
distancia_maxima(D, N, DistanciaMaxima) :-
    N >= 0, % N tiene eue ser positivo 
    distancia_maxima_recursivo(D, N, 0, DistanciaMaxima).

% Predicado recursivo para calcular la distancia máxima
distancia_maxima_recursivo(_, 0, DistanciaAcumulada, DistanciaAcumulada) :- !.
distancia_maxima_recursivo(D, N, DistanciaAcumulada, DistanciaMaxima) :-
    N > 0,
    N1 is N - 1,
    % Caso 1: Cargar un bidón y recorrer con él
    Distancia1 is DistanciaAcumulada + D,
    distancia_maxima_recursivo(D, N1, Distancia1, DistanciaMaxima1),
    % Caso 2: Cargar dos bidones y recorrer con ambos
    Distancia2 is DistanciaAcumulada + 2 * D,
    distancia_maxima_recursivo(D, N1, Distancia2, DistanciaMaxima2),
    % Seleccionar la distancia máxima de ambos casos
    DistanciaMaxima is max(DistanciaMaxima1, DistanciaMaxima2).
