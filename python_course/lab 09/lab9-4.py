# Celem tego zadania jest napisanie funkcji sortującej według algorytmu sortowanie szybkie.
# Aby uprościć zadanie stosujemy wersję algorytm wykorzystującą dodatkową pamięć i nie działającą w miejscu.

# qsort(A):
#     zwróć A jeśli długość A jest < 1

#     pivot <-- ostatni element A
#     X <-- tablica tych elementów z A, które są < pivot
#     Y <-- tablica tych elementów z A, które są == pivot
#     Z <-- tablica tych elementów z A, które są > pivot
#     zwróć konkatenację qsort(X), Y, qsort(Z)

# Napisz funkcję qsort(seq). Parametr seq jest sekwencją, funkcja zwraca listę wartości z seq posortowaną niemalejąco. 
# Wykorzystaj podany wyżej algorytm.

def qsort(A):
    if len(A) <= 1:
        return A
    
    pivot = A[-1]
    X = [_ for _ in A if _ < pivot]
    Y = [_ for _ in A if _ == pivot]
    Z = [_ for _ in A if _ > pivot]
    return qsort(X) + Y + qsort(Z)

A = []
A = qsort(A)
assert A == []

A = [1]
A = qsort(A)
assert A == [1]

A = [4, 3, 2]
A = qsort(A)
assert A == [2, 3, 4]

A = [2, 1, 2, -2]
A = qsort(A)
assert A == [-2, 1, 2, 2]


import sys
sys.setrecursionlimit(4000)
A = list(range(1000, 0, -1))
A = qsort(A)
A = list(range(1, 1001))