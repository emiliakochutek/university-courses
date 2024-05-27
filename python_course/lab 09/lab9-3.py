# Na ile sposobów można wydać resztę 10 mając do dyspozycji monety o nominałach 1, 2 i 5? Oto proste rozwiązanie rekurencyjne z SICP.
# Liczba sposobów, na które można wydać resztę a mając do dyspozycji n monet, jest równa:
#     liczbie sposobów, na które można wydać resztę a mając do dyspozycji wszystkie monety poza pierwszą, plus
#     liczbie sposobów, na które można wydać resztę a − d mając do dyspozycji wszystkie n monet, gdzie d jest wartością pierwszej monety.

# Napisz funkcję rekurencyjną liczba_sposobów_wymiany(a, monety) według podanego wyżej algorytmu. 
# Parametr a oznacza kwotę, parametr monety to sekwencja nominałów.
# Sprawdź jak zmienia się czas wykonania, gdy zastosujesz zapamiętywanie wyników 
# (dekorator @lru_cache() z modułu functools; w tym przypadku monety powinny być obiektem niezmiennym, 
# np. krotką). Ile wywołań potrzeba, aby wyznaczyć liczbę sposobów wydania 200 z monetami 1, 2, 5, 10, 20, 50? 
# Jak zmienia się wynik wraz ze zmianą funkcji z wersji oryginalnej do zapamiętującej? Kiedy zapamiętywanie jest bardziej pomocne:
# gdy monet jest więcej, czy gdy jest ich mniej?

def liczba_sposobów_wymiany(a, monety):
    # przypadki brzegowe:
    if a == 0:
        return 1
    if a < 0 or (a > 0 and not monety):
        return 0
    
    d, *pozostałe_monety = monety
    return liczba_sposobów_wymiany(a, pozostałe_monety) + liczba_sposobów_wymiany(a - d, monety)

## Testy brzegowe
assert liczba_sposobów_wymiany(0, []) == 1
assert liczba_sposobów_wymiany(0, [1, 2, 3]) == 1
assert liczba_sposobów_wymiany(-1, []) == 0
assert liczba_sposobów_wymiany(-1, [1, 2, 3]) == 0

assert liczba_sposobów_wymiany(5, [7, 9]) == 0
assert liczba_sposobów_wymiany(5, [1]) == 1
assert liczba_sposobów_wymiany(5, [1, 2]) == len([5*1, 3*1 + 2, 1 + 2*2])

## https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.2
assert liczba_sposobów_wymiany(100, [1, 5, 10, 25, 50]) == 292