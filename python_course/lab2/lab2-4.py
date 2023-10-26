# Używając klucza ma-li-no-we-bu-ty można zaszyfrować wiadomość wymieniając znaki leżące wewnątrz tych samych sylab klucza: 
# m --> a, a --> m, l --> i, i --> l, itd. Znaki, których nie ma w kluczu, pozostawia się bez zmian. 
# Przykładowo tekst ziemia jest płaska wymaga wymienienia 9 znaków i po zaszyfrowaniu ma postać zlwalm jwsy płmskm. 
# Powtórne zaszyfrowanie przywraca pierwotną postać tekstu.

# 4.1
# Napisz funkcję szyfruj(tekst). Parametr tekst jest łańcuchem. Funkcja zwraca łańcuch będący zaszyfrowanym tekstem tekst według klucza malinowebuty.


def szyfruj(tekst):
    klucz = {'m': 'a',
         'a': 'm',
         'l': 'i',
         'i': 'l',
         'n': 'o',
         'o': 'n',
         'w': 'e',
         'e': 'w',
         'b': 'u',
         'u': 'b',
         't': 'y',
         'y': 't'}
    zaszyfrowany = ''
    for litera in tekst:
        if litera in klucz:
            zaszyfrowany += klucz[litera]
        else:
            zaszyfrowany += litera
    return zaszyfrowany

# W słowniku szyfry_test klucz to tekst do zaszyfrowania, 
# wartość to klucz po zaszyfrowaniu. 
szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

for jawny, tajny in szyfry_test.items():
    assert szyfruj(jawny) == tajny, 'Błąd, powinno być: {} ==> {}'.format(jawny, tajny)


# 4.2
# Napisz dwuparametrową funkcję szyfruj(tekst, klucz). Argumenty klucz i tekst są łańcuchami. 
# Funkcja zwraca łańcuch będący zaszyfrowanym tekstem tekst według klucza klucz. 
# Funkcja powinna mieć argument domyślny klucz ustawiony na wartość 'malinowebuty'.

def szyfruj(tekst, klucz = 'malinowebuty'):
    KLUCZ = {}
    for znak in klucz:
        if (klucz.index(znak) % 2) == 0:
            KLUCZ[znak] = klucz[klucz.index(znak) + 1]
        else:
            KLUCZ[znak] = klucz[klucz.index(znak) - 1]
    zaszyfrowany = ''
    for litera in tekst:
        if litera in KLUCZ:
            zaszyfrowany += KLUCZ[litera]
        else:
            zaszyfrowany += litera
    return zaszyfrowany

# W słowniku szyfry_test klucz to tekst do zaszyfrowania, 
# wartość to klucz po zaszyfrowaniu. 
szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

for jawny, tajny in szyfry_test.items():
    assert szyfruj(jawny) == tajny, 'Błąd, powinno być: {} ==> {}'.format(jawny, tajny)

# Krotki (klucz, tekst_jawny, tekst_tajny)
test_klucz_jawny_tajny = [('ab', 'abc', 'bac'),
                          ('XYUV', 'xVyU', 'xUyV'),
                          ('gaderypoluki', 'gaderypoluki', 'agedyropulik')]

for klucz, jawny, tajny in test_klucz_jawny_tajny:
    assert szyfruj(jawny, klucz) == tajny, 'Klucz {} zamienia {} na {}'.format(klucz, jawny, tajny)


# 4.3
# Klucz uznajemy za prawidłowy, gdy jest różnowartościowy i ma parzystą długość. 
# Rozszerz funkcję szyfruj() z poprzedniego punktu o test czy klucz jest poprawny. 
# W przypadku wykrycia nieprawidłowego klucza funkcja szyfruj() ma wywoływać wyjątek ValueError z komunikatem: nieprawidłowy klucz!.

def szyfruj(tekst, klucz = 'malinowebuty'):
    if (len(klucz) % 2) != 0 or len(set(klucz)) != len(klucz):
        raise ValueError('nieprawidłowy klucz!')
    KLUCZ = {}
    for znak in klucz:
        if (klucz.index(znak) % 2) == 0:
            KLUCZ[znak] = klucz[klucz.index(znak) + 1]
        else:
            KLUCZ[znak] = klucz[klucz.index(znak) - 1]
    zaszyfrowany = ''
    for litera in tekst:
        if litera in KLUCZ:
            zaszyfrowany += KLUCZ[litera]
        else:
            zaszyfrowany += litera
    return zaszyfrowany

# W słowniku szyfry_test klucz to tekst do zaszyfrowania, 
# wartość to klucz po zaszyfrowaniu. 
szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

for jawny, tajny in szyfry_test.items():
    assert szyfruj(jawny) == tajny, f'Błąd, powinno być: {jawny} ==> {tajny}'
    
# Nieprawidłowe klucze do testowania wyjątków.
nieprawidłowe_klucze = ['x', 'xyz', 'xyzx']

for klucz in nieprawidłowe_klucze:
    try:
        szyfruj('abc', klucz)
    except ValueError as err:
        assert str(err) == 'nieprawidłowy klucz!', 'Niewłaściwy komunikat.'
    except Exception as err:
        raise AssertionError('Nieprawidłowy wyjątek {!r}'.format(err))
    else:
        raise AssertionError(f"Brak wyjątku: '{klucz}' nie jest prawidłowym kluczem!")

# Krotki (klucz, tekst_jawny, tekst_tajny)
test_klucz_jawny_tajny = [('ab', 'abc', 'bac'),
                          ('XYUV', 'xVyU', 'xUyV'),
                          ('gaderypoluki', 'gaderypoluki', 'agedyropulik')]

for klucz, jawny, tajny in test_klucz_jawny_tajny:
    assert szyfruj(jawny, klucz) == tajny, f'Klucz {klucz} zamienia {jawny} na {tajny}'
