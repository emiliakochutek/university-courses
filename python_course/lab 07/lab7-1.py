# 1.1
# Napisz funkcję jest_stały(seq). Parametr seq jest sekwencją. Funkcja zwraca True, gdy seq jest ciągiem stałym; 
# w przeciwnym razie False. Wykorzystaj algorytm:

def jest_stały(seq):
    n = len(seq)
    for _ in range(0, n - 1):
        if seq[_] != seq[_ + 1]:
            return False
    return True

assert jest_stały([])
assert jest_stały('')
assert jest_stały('c')
assert not jest_stały('ab')
assert jest_stały('########')
assert jest_stały([-5])
assert jest_stały([3, 3, 3, 3])
assert not jest_stały([1, 1, 1, 2])
assert not jest_stały([1, 0, 0, 0, 0, 0])
assert not jest_stały([1, 2, 5, 8, 7])


# 1.2
# Napisz funkcję jest_rosnący(seq). Parametr seq jest sekwencją. Funkcja zwraca True, 
# gdy seq jest ciągiem rosnącym; w przeciwnym razie False. Wykorzystaj algorytm:

def jest_rosnący(seq):
    n = len(seq)
    for _ in range(0, n - 1):
        if seq[_] >= seq[_ + 1]:
            return False
    return True

assert jest_rosnący([])
assert jest_rosnący('')
assert jest_rosnący('c')
assert jest_rosnący('ab')
assert jest_rosnący('abcdpx')
assert jest_rosnący([-5])
assert jest_rosnący([-5, 10, 100.45, 2**10])
assert not jest_rosnący([1, 1])
assert not jest_rosnący([1, 0])
assert not jest_rosnący([1, 2, 5, 8, 7])


# 1.3
# Napisz funkcję sprawdź_sąsiednie(seq, pred) uogólniającą wzorzec z poprzednich dwóch funkcji. Parametry:
#     seq - sekwencja,
#     pred - funkcja dwuargumentowa.
# Funkcja sprawdź_sąsiednie() zwraca True, gdy wartość pred na każdej parze sąsiednich wartości w seq 
# odpowiada wartości True. W przeciwnym razie zwraca False. Powtórnie napisz funkcje z punktów 1.1, 1.2, 
# ale tym razem wykorzystaj sprawdź_sąsiednie() wraz z odpowiednią funkcją pred().

def sprawdź_sąsiednie(seq, pred):
    n = len(seq)
    for i in range(0, n - 1):
        if not pred(seq[i], seq[i + 1]):
            return False
    return True

def jest_stały(seq):
    return sprawdź_sąsiednie(seq, lambda x, y: x == y)

def jest_rosnący(seq):
    return sprawdź_sąsiednie(seq, lambda x, y: x < y)

assert sprawdź_sąsiednie([], lambda x, y: False)
assert sprawdź_sąsiednie('a', lambda x, y: False)

import random
lst = [random.random() for _ in range(100)]
assert sprawdź_sąsiednie(lst, lambda x, y: True)

s = 'abcdepqr'
assert sprawdź_sąsiednie(s, lambda x, y: x < y)

s = 'abcdepqro'
assert not sprawdź_sąsiednie(s, lambda x, y: x < y)

s = 'uuuuuu'
assert sprawdź_sąsiednie(s, lambda x, y: x == y)

s = 'uuuuuu'
assert sprawdź_sąsiednie(s, lambda x, y: x == y)