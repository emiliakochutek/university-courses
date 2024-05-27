# Napisz jednoparametrowy dekorator @pre_test(pred). Zadaniem dekoratora jest poprzedzenie 
# wywołania dekorowanej funkcji wykonaniem testu pred na jej argumentach.

# z zajec:
def pre_test(pred):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            pred(*args, **kwargs)         # Wywołanie testu pred jako pierwsza linia
            # out = f(*args, **kwargs)    # Wywołanie dekorowanej funkcji
            # return out
            return f(*args, **kwargs)     # skróciłam dwie poprzednie linijki żeby było czytelniej, nie wiem po kiego ta zmienna out xd
        return wrapper
    return dekorator

## chat gpt [nie przechodzi testów z zajęć bo dekorator wykonuje test pred na argumentach dekorowanej funkcji
## przed jej wywołaniem (po prostu inne zastosowanie)]:
# def pre_test(pred):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if pred(*args, **kwargs):
#                 return func(*args, **kwargs)
#             else:
#                 print("Test pred nie został zaliczony.")
#         return wrapper
#     return decorator


def dodatnia(x):
    assert x > 0, f'{x} <= 0'

@pre_test(dodatnia)
def u(a):
    return a**.5

assert u(9) == 3.0
assert u(100) == 10.0
assert dodatnia.__name__ == 'dodatnia', 'Utracono metadane funkcji'

try:
    u(-9)
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')

def jest_nazwą_zmiennej(s):
    assert s.isidentifier(), 'łańcuch nie jest nazwą zmiennej.'
    
@pre_test(jest_nazwą_zmiennej)
def g(s):
    return s.upper()

assert g('a') == 'A'
assert g('x') == 'X'
assert g('x_2') == 'X_2'

try:
    g('2a')
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')

try:
    g('a-3')
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')

def co_najmniej_3(*c):
    assert len(c) > 2, 'mniej niż 3 argumenty'
    
@pre_test(co_najmniej_3)
def h(*c):
    return max(c)

assert h(3, 1, 5, 2) == 5

try:
    h(3, 1)
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')