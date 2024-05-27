# Napisz funkcję fib(n) zwracającą wyraz Fn ciągu Fibonacciego. 
# Funkcja fib() powinna delegować zadanie do innej funkcji, która jest zaimplementowana jako rekurencja ogonowa.

def fib(n):
    def fib_tail(n, a, b):
        if n == 0:
            return a
        a, b = b, a + b
        return fib_tail(n - 1, a, b)
    return fib_tail(n, 0, 1)


assert fib(0) == 0
assert fib(1) == 1
assert [fib(n) for n in [2, 3, 4, 5, 6]] == [1, 2, 3, 5, 8]

# https://www.wolframalpha.com/input?i=fib+100
assert fib(100) == 354224848179261915075

import sys
try:
    fib(sys.getrecursionlimit() + 1)
except RecursionError:
    pass
else:
    raise AssertionError('czy na pewno twoja funkcja jest rekurencyjna?')