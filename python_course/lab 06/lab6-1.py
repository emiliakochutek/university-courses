
# 1.1
# Napisz funkcje w_lewo(), w_prawo() naprzód(). Funkcje muszą modyfikować globalne zmienne x, y, azymut opisujące stan żółwia. Przeprowadź testy.

import math
# from matplotlib import pyplot as plt

x, y, azymut = 0, 0, 0
abs_tol = 1e-9

def w_lewo(kąt):
    global azymut
    azymut += kąt
    
def w_prawo(kąt):
    global azymut
    azymut -= kąt
    
def naprzód(r):
    global x, y
    x += r * math.cos(math.radians(azymut))
    y += r * math.sin(math.radians(azymut))

# Spodziewamy się x == 100, y == 0, azymut == 0
naprzód(100)
assert abs(x - 100) < abs_tol
assert abs(y - 0) < abs_tol
assert azymut == 0

# Spodziewamy się x == 100, y == 0, azymut == 90
w_lewo(90)
assert abs(x - 100) < abs_tol
assert abs(y - 0) < abs_tol
assert azymut == 90

# Spodziewamy się x == 100, y == 100, azymut == 90
naprzód(100)
assert abs(x - 100) < abs_tol
assert abs(y - 100) < abs_tol
assert azymut == 90

# Spodziewamy się x == 0, y == 0, azymut == 0
w_lewo(90 + 45)
naprzód(100 * math.sqrt(2))
assert abs(x - 0) < abs_tol
assert abs(y - 0) < abs_tol
assert azymut == 90 + 90 + 45


# 1.2
# Aby narysować trasę żółwia, należy ją zapamiętać. Zmodyfikuj funkcję naprzód(), tak aby zapamiętywała 
# kolejne punkty trasy żółwia w globalnych listach X, Y. Wówczas współrzędne aktualnego położenie żółwia będą równe X[-1], Y[-1].
   
def naprzód(r):
    global x, y
    x += r * math.cos(math.radians(azymut))
    y += r * math.sin(math.radians(azymut))
    X.append(x)
    Y.append(y)

    
def listy_prawie_równe(lst_1, lst_2, abs_tol=1e-9):
    '''Zwraca True, gdy dla wszystkich odpowiadających sobie wartości x, y
    z obu list zachodzi abs(x - y) < abs_tol. W przeciwnym razie False.'''
    
    return all(abs(x - y) < abs_tol for x, y in zip(lst_1, lst_2))

# Nowy żółw w początku układu.
X, Y, azymut = [0], [0], 0

naprzód(100)
w_lewo(90)
naprzód(100)
w_lewo(135)
naprzód(100 * math.sqrt(2))

assert listy_prawie_równe(X, [0, 100, 100, 0])
assert listy_prawie_równe(Y, [0, 0, 100, 0])

# plt.plot(X, Y)