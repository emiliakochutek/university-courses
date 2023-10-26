# Dokończ definicję funkcji, sprawdź testy.

def c_aryt(a, r, n):
    '''Zwraca listę z wyrazami ciągu arytmetycznego.

    Parametry:
    a -- pierwszy wyraz
    r -- różnica ciągu
    n -- liczba wyrazów

    >>> c_aryt(5, 2, 3)
    [5, 7, 9]
    >>> c_aryt(10, -5, 4)
    [10, 5, 0, -5]
    >>> c_aryt(1.5, 10, 0)
    []
    >>> c_aryt(1.5, 10, 1)
    [1.5]
    >>> c_aryt(1.5, 10, 2)
    [1.5, 11.5]
    >>> sum(c_aryt(1, 1, 100)) == 100 * 101 // 2
    True
    '''

    lista = []
    for liczba in range(n):
        lista.append(a)
        a += r
    return(lista)

import doctest

doctest.testmod(verbose = True)
