# Napisz funkcję wstaw_argumenty(f, *args, **kwargs). Parametr f() jest dowolnym obiektem wywoływalnym. 
# Funkcja zwraca funkcję zachowującą się jak f(), do której wstawiono argumenty pozycyjne 
# args i podawane przez nazwę kwargs. Są to argumenty zamrożone. Do wywołania zwróconej funkcji 
# mogą zostać przekazane argumenty pozycyjne - wtedy w wywołaniu f() następują one po argumentach args. 
# Argumenty podawane przez nazwę również mogą zostać wstawione do wywołania - wtedy dodawane są do kwargs.

def wstaw_argumenty(f, *args, **kwargs):
    def funkcja_z_argumentami(*positional_args, **keyword_args):
        all_args = args + positional_args
        all_kwargs = kwargs.copy()
        all_kwargs.update(keyword_args)
        return f(*all_args, **all_kwargs)
    return funkcja_z_argumentami

# testy
def wymnóż(x, y):
    return x * y

try:
    podwój = wstaw_argumenty(wymnóż, y=2)
except Exception as err:
    raise AssertionError(f'pojawił się wyjątek {err}')

assert podwój(6) == 12

try:
    podstawa16 = wstaw_argumenty(int, base=16)
except Exception as err:
    raise AssertionError(f'pojawił się wyjątek {err}')

assert podstawa16('A') == 10
assert podstawa16('FF') == 15*16 + 15

def f(x, y, z, *, u, v):
    return x, y, z, u, v
    
try: ## Zamrażamy x, z, v.
    g = wstaw_argumenty(f, 1, z=2, v=9)
except Exception as err:
    raise AssertionError(f'pojawił się wyjątek {err}')
    
assert g(3, u=7) == (1, 3, 2, 7, 9)

def f(x, y, *args, **kwargs):
    return x, y, args, kwargs
    
try: 
    g = wstaw_argumenty(f, 1, 2, 3, a=99, b=88)
except Exception as err:
    raise AssertionError(f'pojawił się wyjątek {err}')
    
assert g(0) == (1, 2, (3, 0), dict(a=99, b=88))
assert g() == (1, 2, (3,),  dict(a=99, b=88))
assert g(0, c=77) == (1, 2, (3, 0),  dict(a=99, b=88, c=77))