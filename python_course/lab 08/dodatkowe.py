## Napisz dekorator @zachowaj_metadane()
def zachowaj_metadane(fun):
    def dekorator(f): ## f to będzie wrapper()
        f.__name__ = fun.__name__
        f.__doc__ = fun.__doc__
        return f
    return dekorator

## Testy

def przykładowy_dekorator(f):
    @zachowaj_metadane(f)
    def wrapper(*args, **kwargs):
        out = f(*args, **kwargs)
        return out
    return wrapper

@przykładowy_dekorator
def u(x):
    '''Podwój x'''
    return 2*x
assert u(5) == 10
assert u.__name__ == 'u', 'Utracono nazwę funkcji'
assert u.__doc__ == 'Podwój x', 'Utracono docstring'