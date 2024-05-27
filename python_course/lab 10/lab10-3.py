# Napisz klasę Fib. Obiekt klasy powinien posiadać metody:
#     .__init__() - akceptuje dwie wartości początkowe ciągu a (wartość F0) i b (wartość F1), domyślnie 0 i 1;
#     .indeks() - oblicza rekurencyjnie wyraz Fn ciągu Fibonacciego. Wykorzystaj memoizację: 
# przechowaj obliczone wartości ciągu w słowniku będącym atrybutem self.

class Fib:
    def __init__(self, a=0, b=1):
        self.mem = {0: a, 1: b}

    def indeks(self, n):
        if n in self.mem:
            return self.mem[n]
        
        self.mem[n] = self.indeks(n-2) + self.indeks(n-1)
        return self.mem[n]
        
fib = Fib()
assert [fib.indeks(n) for n in range(6)] == [0, 1, 1, 2, 3, 5]
#https://www.wolframalpha.com/input/?i=fibonacci(100)
assert fib.indeks(100) == 354224848179261915075

fib = Fib(a=2, b=1)
assert [fib.indeks(n) for n in range(6)] == [2, 1, 3, 4, 7, 11]

fib = Fib(a=-1, b=1)
assert [fib.indeks(n) for n in range(6)] == [-1, 1, 0, 1, 1, 2]

