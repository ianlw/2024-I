

/* Base de conocimientos de provincias y sus distritos */
/* Definir listas */

lista(cusco, [cusco, wanchaq, santiago, poroy, saylla,
        ccorca, 'san sebastián', 'san jerénimo']).

lista(paruro, [paruro, yaurisque, paccarectambo, huanoquite,
        omacha, colcha, ccapí, pillpínto]).

/* Definir reglas */
mostrarDistritos([]). % Termina de mostrar cuando alcanza a una lista vacía.
mostrarDistritos([Cabeza|Resto]) :-
    write(Cabeza) , nl, mostrarDistritos(Resto).

mostrarDistritosProvincia(Provincia) :-
    lista(Provincia, Lista), mostrarDistritos(Lista).

