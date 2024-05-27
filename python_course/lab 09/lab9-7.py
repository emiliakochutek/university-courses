# 7.1
# Napisz rekurencyjną funkcję zgadnij_liczbę(a, b). Parametry a, b odpowiadają za zakres, w którym poszukiwana będzie liczba.

# def zgadnij_liczbę_niebinarne(a, b):
#     '''docstring'''
#     środek = (a + b) // 2

#     odpowiedź = input(f"Czy liczba jest równa {środek}? (t/n): ")
#     if odpowiedź == 't':
#         print(f'Twoja liczba to {a}')
#         return
    
#     odpowiedź2 = input(f"Czy liczba jest większa od {środek}? (t/n): ")
#     if odpowiedź2 == 't':
#         a = środek + 1
#     else:
#         b = środek - 1

#     zgadnij_liczbę_niebinarne(a, b)

def zgadnij_liczbę(a, b):
    '''docstring'''
    środek = (a + b) // 2

    odpowiedź = input(f'czy twoja liczba jest większa od {środek}? [tak/nie] ')

    if odpowiedź == 'tak':
        a = środek + 1
    else:
        b = środek
    if a == b:
        print(f'Twoja liczba to {a}')
        return 
    
    zgadnij_liczbę(a, b)


# 7.2
# Napisz rekurencyjną funkcję wyszukiwanie_binarne(x, seq). Parametr x to dowolna wartość, seq - uporządkowana niemalejąco sekwencja. 
# Funkcja zwraca True jeśli x jest wartością w seq, w przeciwnym razie zwraca False. Wykorzystaj rekurencyjny algorytm wyszukiwania binarnego.

# def wyszukiwanie_binarne(x, seq):
#     '''docstring'''
#     jest_w_seq = False
#     if not seq:
#         return jest_w_seq
    
#     a, b = seq[0], seq[-1]
#     środek = (a + b) // 2
#     for _ in seq[a : środek]:
#         if _ == x:
#             jest_w_seq = True
#     a, środek = środek, (środek + b) // 2
#     wyszukiwanie_binarne(x, seq)

def wyszukiwanie_binarne(x, seq):
    '''docstring'''
    if not seq:
        return False
    
    a, b = 0, len(seq) - 1
    środek = (a + b) // 2

    if seq[środek] == x:
        return True
    elif seq[środek] < x:
        return wyszukiwanie_binarne(x, seq[środek + 1:])
    else:
        return wyszukiwanie_binarne(x, seq[:środek])

assert not wyszukiwanie_binarne(1, []), 'Znalazłem 1 w pustej liście.'
assert wyszukiwanie_binarne(1, [1]), 'Nie znalazłem 1 w liście [1]'

LICZBY = [1, 2]

for liczba in LICZBY:
    assert wyszukiwanie_binarne(liczba, LICZBY), 'Nie znalazłem {} w {}'.format(liczba, LICZBY)

for liczba in [0, 3]:
    assert not wyszukiwanie_binarne(liczba, LICZBY), 'Znalazłem {} w {}'.format(liczba, LICZBY)

LICZBY = [5, 7, 11]

for liczba in LICZBY:
    assert wyszukiwanie_binarne(liczba, LICZBY), 'Nie znalazłem {} w {}'.format(liczba, LICZBY)

for liczba in [1, 6, 10, 12]:
    assert not wyszukiwanie_binarne(liczba, LICZBY), 'Znalazłem {} w {}'.format(liczba, LICZBY)

LITERY = 'abcdefghijklmnopqrstuvwxyz'

for litera in LITERY:
    assert wyszukiwanie_binarne(litera, LITERY), 'Nie znalazłem {} w {}'.format(litera, LITERY)

for znak in '123%&':
    assert not wyszukiwanie_binarne(znak, LITERY), 'Znalazłem {} w {}'.format(znak, LITERY)

assert wyszukiwanie_binarne.__doc__, 'Nie napisałeś docstringu :-)'

# 7.3
# Napisz rekurencyjną funkcję znajdź_zero(f, a, b, abs_tol=1e-6). Parametr f jest obiektem wywoływalnym zwracającym wartości rzeczywiste. 
# Odpowiada funkcji, której miejsce zerowe poszukujemy. Parametry a, b to krańce przedziału. Funkcja znajdź_zero() zwraca środek przedziału [a,b], 
# gdy funkcja f() ma w nim wartość zero, lub gdy b - a < abs_tol. Funkcja powinna rzucać ValueError, jeśli f(a) * f(b) >= 0.

def znajdź_zero(f, a, b, abs_tol=1e-6):
    '''docstring'''
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) * f(b) >= 0")

    c = (a + b) / 2

    if abs(b - a) < abs_tol:
        return c

    if f(c) == 0:
        return c
    elif f(a) * f(c) < 0:
        return znajdź_zero(f, a, c, abs_tol)
    else:
        return znajdź_zero(f, c, b, abs_tol)
    

from math import isclose, cos, pi

domyślny_abs_tol = 1e-6

f = lambda x: x
z = znajdź_zero(f, -1, 2)
assert isclose(z, 0, abs_tol=domyślny_abs_tol)

#  cosinus zeruje się w pi/2
z = znajdź_zero(cos, 0, pi)
assert isclose(z, pi / 2, abs_tol=domyślny_abs_tol)

#  https://www.wolframalpha.com/input/?i=x%5E3%20-%20x%20-%202%20%3D%200
f = lambda x: x**3 - x - 2
z = znajdź_zero(f, 0, 2, abs_tol=1e-11)
assert isclose(z, 1.52137970680457, abs_tol=1e-11)


f = lambda x: 1 + x**2

try:
    znajdź_zero(f, 1, 100)
except ValueError:
    pass
except Exception:
    raise AssertionError('Nieprawidłowy rodzaj błędu.')
else:
    raise AssertionError('Brak wyjątku ValueError. Funkcja nie ma zera w przedziale.')

assert znajdź_zero.__doc__, 'Nie napisałeś docstringu :-)'