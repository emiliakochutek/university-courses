# 3.1
# Teraz stan żółwia przechowywany jest w trzech niepowiązanych obiektach: X, Y i azymut. 
# Wygodniej będzie, gdy obiekty te umieścimy w jednej strukturze danych, np. w słowniku. 
# Słownik ten może mieć trzy klucze: 'X', 'Y' i 'azymut' odpowiadające zmiennym X, Y, azymut. 
# Wówczas nazwę słownika możemy utożsamić z imieniem żółwia. Dzięki tej zmianie będziemy mogli operować równocześnie dowolną liczbą żółwi.
# Napisz nowe definicje funkcji naprzód(), w_lewo(), w_prawo() zgodnie z podanymi niżej testami. 
# Zauważ, że funkcje te mają teraz dodatkowy parametr wskazujący na słownik reprezentujący żółwia.

import math
abs_tol = 1e-9


tolek = {'X': [0],
         'Y': [0],
         'azymut': 0}

def naprzód(żółw, r):
    żółw['X'].append(r * math.cos(math.radians(żółw["azymut"])))
    żółw['Y'].append(r * math.sin(math.radians(żółw["azymut"])))

def w_lewo(żółw, kąt):
    żółw['azymut']+= kąt

def w_prawo(żółw, kąt):
    żółw['azymut'] -= kąt

def listy_prawie_równe(lst_1, lst_2, abs_tol=1e-9):
    '''Zwraca True, gdy dla wszystkich odpowiadających sobie wartości x, y
    z obu list zachodzi abs(x - y) < abs_tol. W przeciwnym razie False.'''

    return all(abs(x - y) < abs_tol for x, y in zip(lst_1, lst_2))

naprzód(tolek, 100)
w_lewo(tolek, 90)
naprzód(tolek, 100)
w_lewo(tolek, 135)
naprzód(tolek, math.sqrt(2) * 100)
assert listy_prawie_równe(tolek['X'], [0, 100, 100, 0])
assert listy_prawie_równe(tolek['Y'], [0, 0, 100, 0])
assert tolek['azymut'] == 90 + 135

# plt.plot(tolek['X'], tolek['Y'])