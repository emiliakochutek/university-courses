# Napisz jednoparametrowy dekorator @klucz(k). Parametr k jest funkcją lub (domyślnie) 
# wartością None. Funkcja @klucz() dekoruje jednoargumentowe funkcje zwracające minimum 
# lub maksimum z sekwencji. Jeżeli k ma wartość None, to dekorowanie nie ma żadnego wpływu 
# na dekorowaną funkcję. Jeśli k jest funkcją, to wyszukiwanie minimum/maksimum odbywa 
# się względem wywołań k na wartościach sekwencji.

import functools

def klucz(k = None):
    def dekorator(f):
        if k is None:
            return f
        
        @functools.wraps(f)
        def wrapper(seq):
            ## Dekoracja seq
            seq = [(k(a), i, a) for i, a in enumerate(seq)]
            ## Znajdź maksimum
            mx = f(seq)
            ## Usuń dekorację z seq
            return mx[-1]
        return wrapper
    return dekorator

# Owoce

owoce = [('jabłko', 1), ('arbuz', 10), ('banan', 4), ('gruszka', 6)]


def drugi_element_pary(para):
    return para[1]


@klucz(drugi_element_pary)
def maksimum(seq):
    '''Zwraca maksimum z sekwencji seq'''
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    
    mx = seq[0]
    
    for a in seq[1:]:
        if a > mx:
            mx = a
    
    return mx


assert maksimum(owoce) == ('arbuz', 10)


@klucz(drugi_element_pary)
def minimum(seq):
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    
    mn = seq[0]
    
    for a in seq[1:]:
        if a < mn:
            mn = a
    
    return mn


assert minimum(owoce) == ('jabłko', 1)


# Najdalszy punkt od początku układu współrzędnych

def sq_norm(p):
    x, y = p
    return x**2 + y**2


@klucz(sq_norm)
def maksimum(seq):
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    
    mx = seq[0]
    
    for a in seq[1:]:
        if a > mx:
            mx = a
    
    return mx


seq = [(0, 0), (0, 20), (1, 1), (10, -10)]
assert maksimum(seq) == (0, 20)


# Najdłuższe słowo

@klucz(len)
def maksimum(seq):
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    
    mx = seq[0]
    
    for a in seq[1:]:
        if a > mx:
            mx = a
    
    return mx

lst = 'ala ma kota i psa'.split()
assert maksimum(lst) == 'kota'


# Test czy utracono metadane

assert maksimum.__name__ == 'maksimum', 'Utracono metadane funkcji.'