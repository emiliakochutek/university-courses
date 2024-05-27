# 2.1
# Funkcja choice() z modułu random losuje element z niepustej sekwencji.

from random import choice

# Losowa wartość z listy
lst = [1, 2, 3, 4, 5]
choice(lst)

# Losowa wartość z łańcucha
s = 'ala ma kota'
choice(s)

# Dziesięć losowań z łańcucha znaków
# zapamiętanych w liście.
s = 'abc'
[choice(s) for _ in range(10)]


# 2.2
# Napisz funkcję losuj_z_urny(liczba_losowań, zwracanie, **kule) symulującą losowanie z urny. Opis parametrów:
#     liczba_losowań -- liczba całkowita, domyślnie 1. Wyznacza liczbę losowań z urny.
#     zwracanie -- True lub False, domyślnie True. Decyduje o tym, czy losowania są prowadzone ze zwracaniem (domyślnie tak).
#     kule -- przyjmuje argumenty postaci klucz=wartość, gdzie
#         klucz -- łańcuch będący kolorem kuli,
#         wartość -- liczba całkowita nieujemna określająca liczbę kul danego koloru w urnie.
# Funkcja zwraca listę kolejno wylosowanych kul. Jeśli losowanie jest bez zwracania i liczba_losowań przewyższa liczbę kul w urnie,
# to funkcja rzuca wyjątek ValueError z komunikatem 'Liczba losowań bez zwracania większa niż liczba kul.'


def losuj_z_urny(liczba_losowań = 1, zwracanie = True, **kule):
    if not zwracanie and liczba_losowań > sum(kule.values()):
        raise ValueError('Liczba losowań bez zwracania większa niż liczba kul.')
    
    urna = []
    
    for kula, liczność in kule.items():
        urna.extend(liczność * [kula])
    
    worek = [] # wylosowane kule
    
    for _ in range(liczba_losowań):
        kula = choice(urna)
        worek.append(kula)
        
        if not zwracanie:
            urna.remove(kula)
    
    return worek
    


from collections import Counter

assert losuj_z_urny(biała=10) == ['biała']

kule = dict(b=2, c=1, z=7)

assert Counter(losuj_z_urny(10, zwracanie=False, **kule)) == Counter(b=2, c=1, z=7)

try:
    losuj_z_urny(liczba_losowań=11, zwracanie=False, **kule)
except ValueError as err:
    komunikat = str(err)
    if komunikat != 'Liczba losowań bez zwracania większa niż liczba kul.':
        raise AssertionError('Rzuca wyjątek ale z nieprawidłowym komunikatem.')
else:
    raise AssertionError('Należało rzucić wyjątek. Losowań jest za dużo.')