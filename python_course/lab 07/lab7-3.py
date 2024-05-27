# Napisz funkcję automat_losujący(zwracanie, **kule). Funkcja zwraca bezparametrową funkcję automat() 
# symulującą losowanie kul z urny. Opis parametrów:
#     zwracanie -- True lub False, domyślnie True. Decyduje o tym, czy losowania są prowadzone ze zwracaniem (domyślnie tak).
#     kule -- przyjmuje argumenty postaci kolor=krotność, gdzie
#         kolor -- łańcuch będący kolorem kuli,
#         krotność -- liczba całkowita nieujemna określająca liczbę kul danego koloru w urnie.
# Każde wywołanie funkcji automat() losuje kulę z urny a następnie zwraca listę wylosowanych dotąd kul. 
# Jeśli urna jest pusta, automat() powinien rzucać wyjątek LookupError z komunikatem 'urna jest pusta.'

import random

def automat_losujący(zwracanie = True, **kule):
    urna = []
    for kula, k in kule.items():
        urna.extend(k * [kula])
        
    worek = [] ## na wylosowane kule
    def automat():
        if not urna:
            raise LookupError('urna jest pusta.')
        kula = random.choice(urna)
        worek.append(kula)
        if not zwracanie:
            urna.remove(kula)
        return worek
    return automat


# 3 białe, 2 czarne, jedna zielona
kule = dict(b=3, c=2, z=1)

# Robot losujący bez zwracania
bot = automat_losujący(zwracanie=False, **kule)

# 5 losowań, w urnie pozostała jedna kula
for _ in range(5):
    bot()

# Ostatnie losowanie. Na wyjściu w kolejności alfabetycznej
# powinny znaleźć się 3 białe, dwie czarne i jedna zielona.
assert sorted(bot()) == list('bbbccz')

# Urna jest pusta, nie da się losować dalej
try:
    bot()
except LookupError as err:
    assert str(err) == 'urna jest pusta.', 'Nieprawidłowy komunikat błędu.'
except Exception:
    raise AssertionError('Nieprawidłowy wyjątek.')
else:
    raise AssertionError('Urna powinna być pusta!')
    
# Robot losujący ze zwracaniem. Może losować bez końca.
bot = automat_losujący(**kule)

# Losujemy 1000 razy:
for _ in range(999):
    bot()

lista_wylosowanych = bot()

# Przy trzech białych, dwóch czarnych i jednej zielonej w urnie
# jest mało prawdopodobne (ile wynosi to pstwo?), że po 1000 losowaniach
# wylosowanych białych będzie mniej niż zielonych.
assert lista_wylosowanych.count('b') >= lista_wylosowanych.count('z'), '''Mało prawdopodobny wynik.
Sprawdź jeszcze raz kod funkcji.'''

## Test, czy listy, do których boty zbierają wyniki,
## są różne.
bot1 = automat_losujący(b=1)
bot2 = automat_losujący(c=1)
bot1()
assert bot2() == ['c']