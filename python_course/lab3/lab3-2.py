# Algorytm Euklidesa wygląda następująco. Niech r1, r2 będą dodatnimi liczbami całkowitymi. 
# Dzielimi r1 przez r2 z resztą uzyskując r1=q2⋅r2+r3, gdzie q2>0, r3∈{0,1,…,r2−1}. 
# Jeśli okaże się, że r3≠0, to znów wykonujemy dzielenie z resztą, tym razem r2 przez r3: r2=q3⋅r3+r4. 
# Następnie dzielimy r3 przez r4, o ile oczywiście r4≠0, uzyskując r3=q4⋅r4+r5, itd. Ciąg reszt r2,r3,r4,… ma wartości nieujemne, 
# jest silnie malejący i może być obliczany tak długo dopóki uzyskiwane reszty są dodatnie. 
# W konsekwencji musi osiągnąć w końcu wartość zero i algorytm się wtedy zatrzyma.

# 2.1
# Napisz funkcję euklides(a, b). Parametry a, b to dodatnie liczby całkowite. Przyjmując, że a i b to, odpowiednio r1
# i r2, funkcja zwraca w postaci listy zdefiniowane wyżej liczby r1,r2,r3,r4,… aż do końcowego zera włącznie

def euklides(a, b):
    '''funkcja zwraca w postaci listy liczby r1,r2,r3,r4,… aż do końcowego zera włącznie'''
    reszty = [a, b]  # Inicjalizacja listy reszt
    while b != 0:
        a, b = b, a % b
        reszty.append(b)
    return reszty

assert euklides(1, 1) == [1, 1, 0]
assert euklides(2, 1) == [2, 1, 0]
assert euklides(1, 2) == [1, 2, 1, 0]
assert euklides(17, 13) == [17, 13, 4, 1, 0]
assert euklides.__doc__, 'Nie napisałeś docstringu!'


# 2.2
# Wyznacz parę liczb a, b z zakresu 2 <= b < a <= 1000, która wymaga największej liczby dzieleń w algorytmie euklidesa.

mx = 0

for b in range(2, 1000):
    for a in range(b + 1, 1001):
        d = len(euklides(a, b))
        if d > mx:
            a0, b0 = a, b #kandydaci do najdluzszego ciagu

