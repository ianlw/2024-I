

factorial(0, 1). % caso base.
factorial(N, F) :- N>0, N1 is N - 1, factorial(N1, F1), F is N * F1. % caso recurrente.

nrodigitos(0, 0).
nrodigitos(N, R) :- N>0, N1 is N // 10, nrodigitos(N1, R1), R is 1 + R1.

nrodigitosimp(0, 0).
nrodigitosimp(N, I) :- N>0, R is N mod 2, N1 is N // 10, nrodigitosimp(N1, I1), I is R + I1.

mcd(A, B, M) :- R is A mod B, R =:= 0, M is B.
med(A, B, M) :- R is A mod B, R >0, mcd(B, R, M1), M is M1.

fib(0, 1).
fib(1, 1).
fib(N, F) :- N>1, N1 is N-1, N2 is N-2, fib(N1, F1), fib(N2, F2), F is F1 + F2.
