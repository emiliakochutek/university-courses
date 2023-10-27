# Sito Eratostenesa to algorytm pozwalający na wyznaczenie wszystkich liczb pierwszych nie przekraczających zadanej liczby naturalnej n. 
# Algorytm ten działa następująco. Zakładając, że została wybrana liczba naturalna n > 1, zaczynamy od utworzenia listy liczb 2, 3, ..., n. 
# Następnie skreślamy z listy wszystkie większe do 2 wielokrotności 2, przesuwamy się do pierwszej nieskreślonej liczby (będzie to 3) 
# i skreślamy wszystkie jej wielokrotności od niej większe,
# znów przesuwamy się do pierwszej nieskreślonej liczby (teraz będzie to 5) i skreślamy wszystkie jej 
# wielokrotności od niej większe, itd. aż dojdziemy do końca listy.

# Przykładowo, dla n równego 10 uzyskamy
# 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2, 3, 5, 7, 9,
# 2, 3, 5, 7,
# dostając finalnie liczby pierwsze nie przekraczające 10.

# 3.1
# Napisz funkcję sito(n). Parametr n jest liczbą naturalną większą od 1. Funkcja zwraca listę liczb pierwszych mieszczących 
# się w zakresie od 2 do n. Funkcja powinna realizować opisany wyżej algorytm.

# Rozwiązanie #1
def sito(n):
    '''Parametr n jest liczbą naturalną większą od 1. Funkcja zwraca listę liczb pierwszych mieszczących 
    się w zakresie od 2 do n. Funkcja powinna realizować opisany wyżej algorytm.'''
    lst = list(range(2, n + 1))
    i = 0
    # i - pozycja liczby pierwszej, j - pozycja nastepnej liczby
    while i < len(lst):
        pierwsza = lst[i]
        j = i + 1
        while j < len(lst):
            nastepna = lst[j]
            if nastepna % pierwsza == 0:
                del lst[j]
            else:
                j += 1
        i += 1
    return lst

# Rozwiązanie #2
def sito(n):
    '''Parametr n jest liczbą naturalną większą od 1. Funkcja zwraca listę liczb pierwszych mieszczących 
    się w zakresie od 2 do n. Funkcja powinna realizować opisany wyżej algorytm.'''
    lst = list(range(2, n + 1))
    for num in lst:
        if num is not None:
            for crossed in range(2 * num, n + 1, num):
                lst[crossed - 2] = None
    return [num for num in lst if num is not None]


assert sito(2) == [2]
assert sito(10) == [2, 3, 5, 7]

# https://www.wolframalpha.com/input/?i=100th+prime
assert sito(541)[-1] == 541

# http://www.wolframalpha.com/input/?i=sum+of+primes+%3C+1000
assert sum(sito(1000)) == 76127

assert sito.__doc__, 'Nie napisałeś docstringu!'

#https://www.wolframalpha.com/input/?i=pi(10**6)
assert len(sito(10**6)) == 78498


# 3.2
# Napisz funkcję pi(n) zwracającą liczbę liczb pierwszych nie przekraczających n. Wykorzystaj funkcję sito().

def pi(n):
    return len(sito(n))

assert pi(0) == 0
assert pi(1) == 0
assert pi(2) == 1
assert pi(10) == 4

# https://www.wolframalpha.com/input/?i=number+of+primes+less+than+10000
assert pi(10000) == 1229


# 3.3
# Dwie liczby pierwsze, których różnica wynosi 2 nazywamy bliźniaczymi. Napisz funkcję bliźniacze(n).
# Funkcja zwraca listę par (krotek) wszystkich liczb bliźniaczych nie przekraczających n.

def bliźniacze(n):
    '''Funkcja zwraca listę par (krotek) wszystkich liczb bliźniaczych nie przekraczających n.'''
    liczby_pierwsze = sito(n)
    wyniki = []
    for każda in range(len(liczby_pierwsze) - 1):
        if liczby_pierwsze[każda + 1] - liczby_pierwsze[każda] == 2:
            wyniki.append((liczby_pierwsze[każda], liczby_pierwsze[każda + 1]))
    return wyniki

assert bliźniacze(20) == [(3, 5), (5, 7), (11, 13), (17, 19)]

# http://www.wolframalpha.com/input/?i=number+of+twin+primes+less+than+200
assert len(bliźniacze(200)) == 15

assert bliźniacze.__doc__, 'Nie napisałeś docstringu!'


# Ile jest par liczb bliźniaczych mniejszych od miliona?
print(len(bliźniacze(10**6)))


# 3.4
# Zgodnie ze słynną hipoteza Goldbacha każda liczba parzysta większa od 2 jest sumą dwóch liczb pierwszych.
# Zweryfikuj tę hipotezę dla liczb nie przekraczających miliona.

def zweryfikuj_goldbacha(n):
    liczby_pierwsze = sito(n)
    for liczba in range(4, n+1, 2):  # iterujemy tylko po liczbach parzystych większych od 2
        znaleziono_sumę = False
        for pierwsza in liczby_pierwsze:
            if pierwsza > liczba:
                break  # przekroczyliśmy wartość liczby, nie ma dalszych możliwości
            druga = liczba - pierwsza
            if druga in liczby_pierwsze:
                znaleziono_sumę = True
                break
        if not znaleziono_sumę:
            return False  # hipoteza Goldbacha nie jest spełniona dla tej liczby
    return True  # hipoteza Goldbacha jest spełniona dla wszystkich liczb


print(zweryfikuj_goldbacha(10**4))