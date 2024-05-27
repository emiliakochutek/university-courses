# 1.1
# Napisz bezparametrowy dekorator @rejestruj. Działanie dekoratora 
# polega na dodaniu dekorowanej funkcji do globalnej zmiennej rejestr.

def rejestruj(funkcja):
    rejestr.append(funkcja)
    return funkcja

rejestr = []

@rejestruj
def dodaj(x, y):
    return x + y

def średnia(*seq):
    if not seq:
        raise ValueError('ciąg pusty nie ma średniej.')
    
    return sum(seq) / len(seq)

@rejestruj
def odejmij(x, y):
    return x - y

assert rejestr == [dodaj, odejmij]


# 1.2
# Napisz jednoparametrowy dekorator @rejestruj(rejestr). Działanie dekoratora 
# polega na dodaniu dekorowanej funkcji do zmiennej rejestr przekazywanej jako argument dekoratora.

def rejestruj(rejestr):
    def dekorator(f):
        rejestr.append(f)
        return f
    return dekorator

arytmetyczne = []
inne = []

@rejestruj(arytmetyczne)
def dodaj(x, y):
    return x + y

@rejestruj(inne)
def średnia(*seq):
    if not seq:
        raise ValueError('ciąg pusty nie ma średniej.')
    
    return sum(seq) / len(seq)

@rejestruj(arytmetyczne)
def odejmij(x, y):
    return x - y

assert arytmetyczne == [dodaj, odejmij]
assert inne == [średnia]
