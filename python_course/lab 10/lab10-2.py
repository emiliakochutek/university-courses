# Napisz klasę Kwadraty.
# Obiekt klasy reprezentuje nieskończony ciąg kwadratów kolejnych nieujemnych liczb całkowitych 0, 1, 4, 9, 16, ...
# Wywołanie metody .następny() zwraca kolejną wartość ciągu.

class Kwadraty:

    def __init__(self):
        self._indeks = 0 

    def następny(self):
        wynik = self._indeks ** 2
        self._indeks += 1
        return wynik


kwadraty = Kwadraty()
assert kwadraty.następny() == 0
assert kwadraty.następny() == 1
assert kwadraty.następny() == 4
assert [kwadraty.następny() for _ in range(5)] == [9, 16, 25, 36, 49]