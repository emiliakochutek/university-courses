# 2.1
# Napisz program, który narysuje
#     kwadrat,
#     trójkąt równoboczny,
#     pięciokąt foremny.
# Długość krawędzi każdej figury niech będzie równa 1.

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
    X.append(x)
    Y.append(y)
    
X, Y, azymut = [0], [0], 0

def kwadrat():
    for _ in range(4):
        naprzód(1)
        w_prawo(90)

    
# plt.plot(X, Y)


# 2.2
# Napisz funkcję wielokąt_foremny(n, bok). Funkcja przesuwa żółwia wzdłuż boków wielokąta foremnego o n bokach i boku długości bok.

def wielokąt_foremny(n, bok):
    kąt = 360 / n

    for _ in range(n):
        naprzód(bok)
        w_prawo(kąt)

# 2.3
# Jedna z najprostszych procedur w geometrii żółwia wygląda tak:

def wielokąt(bok, kąt):
    while True:
        naprzód(bok)
        w_prawo(kąt)

# Na podstawie funkcji wielokąt() napisz funkcję wielokąt_ze_stopem(bok, kąt). Ma to być tak naprawdę ta sama funkcja, 
# ale z pętlą skończoną. Koniec pętli ma wypadać dokładnie w tym momencie, w którym krzywa żółwiowa się zamyka.

def wielokąt_ze_stopem(bok, kąt):
    for _ in range(360 // kąt + 1):
        naprzód(bok)
        w_prawo(kąt)
