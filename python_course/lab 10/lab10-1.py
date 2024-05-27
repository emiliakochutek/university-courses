# Napisz klasę PrędkośćŚrednia. 
# Instancje tej klasy mają przechowywać i aktualizować prędkość średnią punktu na podstawie przebytej drogi i zużytego czasu.

# Do interfejsu klasy należą atrybuty:
#     droga -- wartość liczbowa określająca przebytą drogę;
#     czas -- wartość liczbowa określająca czas zużyty na przebycie drogi;
#     prędkość_średnia -- prędkość średnia punktu;
# i metoda dodaj_odcinek() -- aktualizuje atrybuty na podstawie nowych danych.

# Klasa powinna implementować metody:
#     __init__(self) -- inicjalizuje atrybuty droga i czas na zero.
#     dodaj_odcinek(self, droga, czas) -- aktualizuje wartości atrybutów droga i czas. 
# Ponadto oblicza prędkość średnią i przypisuje ją do atrybutu prędkość_średnia.

class PrędkośćŚrednia:
    
    def __init__(self):
        self.droga = 0
        self.czas = 0

    def dodaj_odcinek(self, droga, czas):
        self.droga += droga
        self.czas += czas
        self.prędkość_średnia = self.droga / self.czas

p = PrędkośćŚrednia()

assert p.droga == 0
assert p.czas == 0

p.dodaj_odcinek(droga=30, czas=15)

assert p.droga == 30
assert p.czas == 15
assert p.prędkość_średnia == 2.0

p.dodaj_odcinek(czas=35, droga=170)

assert p.droga == 200
assert p.czas == 50
assert p.prędkość_średnia == 4.0