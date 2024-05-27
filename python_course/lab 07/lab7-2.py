# Celem tego zadania jest napisanie nowej wersji funkcji szyfrującej z ćwiczeń II.

# 2.1
# Napisz funkcję wykonaj_klucz(klucz). Parametr klucz jest łańcuchem. Funkcja zwraca słownik par k: v, gdzie

#     k -- znak łańcucha klucz,
#     v -- znak, na który k jest wymieniany.

# Prawidłowy klucz, to taki niepusty łańcuch znaków, który jest różnowartościowy i ma parzystą długość. 
# W przypadku wykrycia nieprawidłowego klucza funkcja ma wywoływać wyjątek ValueError z komunikatem: nieprawidłowy klucz..

def wykonaj_klucz(klucz):
    ## Test poprawności klucza
    n = len(klucz)
    if not klucz or n % 2 == 1 or len(set(klucz)) < n:
        raise ValueError('nieprawidłowy klucz.')
    ## Konstrukcja klucza
    słownik_wymian = {}
    for i, znak in enumerate(klucz):
        if i % 2 == 0:
            słownik_wymian[znak] = klucz[i + 1]
        else:
            słownik_wymian[znak] = klucz[i - 1]
    return słownik_wymian
    
    
klucz = 'abcd'
assert wykonaj_klucz(klucz) == dict(a='b', b='a', c='d', d='c')

klucz = 'malinowebuty'
assert wykonaj_klucz(klucz) == dict(m='a', a='m', l='i', i='l',
                                    n='o', o='n', w='e', e='w',
                                    b='u', u='b', t='y', y='t')

nieprawidłowe_klucze = ['', 'x', 'xyz', 'xyzx']

for klucz in nieprawidłowe_klucze:
    try:
        wykonaj_klucz(klucz)
    except ValueError as err:
        assert str(err) == 'nieprawidłowy klucz.', 'Niewłaściwy komunikat.'
    else:
        raise AssertionError("'{}' nie jest prawidłowym kluczem!".format(klucz))
    

# 2.2
# Napisz funkcję wykonaj_szyfrator(klucz). Parametr klucz jest łańcuchem domyślnie ustawionym na 'malinowebuty'.
# Funkcja zwraca funkcję szyfrator(tekst). Parametr tekst jest łańcuchem. szyfrator() ma szyfrować tekst według 
# klucza zwróconego przez wykonaj_klucz(). Słownik ten powinien być obliczany przed definicją funkcji szyfrator(), 
# a zatem ma znajdować się w jej domknięciu. Uwaga: Odwoływanie sie do słownika jest szybsze niż odwoływanie się do sekwencji. 
# Klucz, który wprowadza użytkownik jest łańcuchem, a więc sekwencją. Klucz w łańcuchu można przerobić na słownik wymian, 
# ale przeróbka ta jest kosztowna. Nasza optymalizacja polega na tym, że przerabiamy łańcuch na słownik tylko raz -- 
# w momencie wywołania wykonaj_szyfrator(). Zwrócony szyfrator() zawiera w domknięciu już nie łańcuch lecz słownik, 
# z którego będzie korzystać szybciej niż z łańcucha. Efekt tej optymalizacji nietrudno sprawdzić przeprowadzając eksperyment. 
# Możesz wykorzystać do tego wbudowane funkcje %time, %timeit lub dekorator raportujący czas wykonania.

def wykonaj_szyfrator(klucz = 'malinowebuty'):
    słownik_wymian = wykonaj_klucz(klucz)
    def szyfrator(tekst):
        tajny = []
        for znak in tekst:
            tajny.append(słownik_wymian.get(znak, znak))
        return ''.join(tajny)
    return szyfrator

szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

try:
    malinowebuty = wykonaj_szyfrator()
except TypeError:
    raise AssertionError('Czy uczyniłeś "malinowebuty" wartością domyślną?')

for jawny, tajny in szyfry_test.items():
    assert malinowebuty(jawny) == tajny, 'Błąd, powinno być: {} ==> {}'.format(jawny, tajny)

test_klucz_jawny_tajny = [('ab', 'abc', 'bac'),
                          ('XYUV', 'xVyU', 'xUyV'),
                          ('gaderypoluki', 'gaderypoluki', 'agedyropulik')]

for klucz, jawny, tajny in test_klucz_jawny_tajny:
    szyfruj = wykonaj_szyfrator(klucz)
    assert szyfruj(jawny) == tajny, 'Klucz {} zamienia {} na {}'.format(klucz, jawny, tajny)