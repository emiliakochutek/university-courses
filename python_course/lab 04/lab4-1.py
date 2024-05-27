# 1.1
# Dwa pierwsze wyrazy w klasycznym ciągu Fibonacciego to 0 i 1:
# f0 = 0,   f1 = 1,   fn+2 = fn + fn+1,   n⩾0

# Zmieniając wartości tych wyrazów, zmienisz również ciąg. Napisz funkcję fib(n, a, b). Parametry n, a, b to liczby całkowite, 
# przy czym zakładamy, że n jest nieujemna. Funkcja zwraca wyraz fn (parametr n jest indeksem wyrazu) ciągu Fibonacciego 
# zdefiniowanego przez dwa pierwsze wyrazy a, b. Parametry a i b powinny być ustawione domyślnie na 0 i 1.

def fib(n, a = 0, b = 1):
    for _ in range(n):
        a, b = b, a + b
    return a

assert [fib(n) for n in range(6)] == [0, 1, 1, 2, 3, 5]

#https://www.wolframalpha.com/input/?i=fibonacci(100)
assert fib(100) == 354224848179261915075

assert [fib(n, 2, 1) for n in range(6)] == [2, 1, 3, 4, 7, 11]
assert [fib(n, b=1, a=-1) for n in range(6)] == [-1, 1, 0, 1, 1, 2]


# 1.2
# Ciąg Tribonacciego definiujemy następująco. Jego pierwsze trzy wyrazy to 0, 0, 1. Każdy wyraz następny jest sumą trzech poprzednich. 
# Napisz funkcję trib(n, a, b, c). Parametry n, a, b, c to liczby całkowite, przy czym zakładamy, że n jest nieujemna. 
# Funkcja zwraca wyraz o indeksie n ciągu Tribonacciego. Parametry a, b, c powinny mieć wartości domyślne 0, 0 i 1.
# a, b, c -> b, c, d --> a.b b.c c.a+b+c

def trib(n, a = 0, b = 0, c = 1):
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a

assert [trib(n) for n in range(10)] == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

# http://oeis.org/A000073
assert [trib(n) for n in range(38)] == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274,
                                              504, 927, 1705, 3136, 5768, 10609, 19513,
                                              35890, 66012, 121415, 223317, 410744,
                                              755476, 1389537, 2555757, 4700770, 8646064,
                                              15902591, 29249425, 53798080, 98950096,
                                              181997601, 334745777, 615693474, 1132436852]

assert [trib(n, -1, 0, 1) for n in range(10)] == [-1, 0, 1, 0, 1, 2, 3, 6, 11, 20] 


# 1.3
# Napisz funkcję fib_ogólny(n, a, b, *c). Parametr n reprezentuje nieujemną liczbę całkowitą, a, b, c to wyrazy inicjujące ogólny ciąg Fibonacciego, 
# przy czym a, b to dwa pierwsze wyrazy, c to dowolnej długości sekwencja kolejnych wyrazów. Każdy kolejny wyraz ciągu to suma N poprzednich, 
# gdzie N jest liczbą wyrazów inicjujących. Funkcja zwraca wyraz ciągu o indeksie n.

def fib_ogólny(n, a, b, *c):
    for _ in range(n):
        a, b, *c = b, *c, a + b + sum(c)
    return a

assert [fib_ogólny(n, 1, 2) for n in range(6)] == [1, 2, 3, 5, 8, 13]
assert [fib_ogólny(n, 1, 2, 3, -5) for n in range(10)] == [1, 2, 3, -5, 1, 1, 0, -3, -1, -3]

assert fib_ogólny(100, *range(100)) == sum(range(100))

try:
    fib_ogólny(5)
except TypeError:
    pass
else:
    raise AssertionError('Za mało argumentów startowych.')

try:
    fib_ogólny(5, 1)
except TypeError:
    pass
else:
    raise AssertionError('Za mało argumentów startowych.')