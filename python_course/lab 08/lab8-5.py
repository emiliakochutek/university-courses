# Napisz jednoparametrowy dekorator @post_test(pred). Zadaniem dekoratora jest wykonanie 
# testu pred na wartości zwróconej przez wywołania dekorowanej funkcji.

from functools import wraps

def post_test(pred):
    def dekorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            out = f(*args, **kwargs)
            pred(out)
            return out
        return wrapper
    return dekorator


def dodatnia(x):
    assert x > 0, f'{x} <= 0'

@post_test(dodatnia)
def u(a):
    return a - 10

assert u(18) == 8
assert u(100) == 90
assert dodatnia.__name__ == 'dodatnia', 'Utracono metadane funkcji'

try:
    u(9)
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')

def jest_nazwą_zmiennej(s):
    assert s.isidentifier(), 'łańcuch nie jest nazwą zmiennej.'
    
@post_test(jest_nazwą_zmiennej)
def g(s):
    return ''.join(s.split())

assert g('a b') == 'ab'
assert g('x\n2') == 'x2'
assert g('x_2') == 'x_2'

try:
    g('a + b')
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

def co_najmniej_3(c):
    assert len(c) > 2, 'mniej niż 3 wartości'
    
@post_test(co_najmniej_3)
def h(n):
    return (n,) if n <= 0 else [d for d in range(1, n + 1) if n % d == 0]

assert h(6) == [1, 2, 3, 6]
assert h(10) == [1, 2, 5, 10]

try:
    h(5)
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')

try:
    h(-5)
except AssertionError:
    pass
else:
    raise AssertionError('Funkcja nie rzuciła wyjątku AssertionError')