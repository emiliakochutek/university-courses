# Interpretacja częstościowa prawdopodobieństwa. Dane jest doświadczenie losowe. Chcemy wyznaczyć prawdopodobieństwo zajścia pewnego 
# wyniku tego doświadczenia losowego. W interpretacji częstościowej wykonujemy to doświadczenie wielokrotnie i zliczamy, 
# ile razy otrzymaliśmy interesujący nas wynik. Jeśli doświadczenie powtórzyliśmy N razy, wynik wypadł k razy i powtórzenia były niezależne, 
# to prawdopodobieństwo badanego wyniku szacujemy na k/N
# Podane niżej zadania rozwiąż stosując częstościową interpretację prawdopodobieństwa. Wyniki potwierdź rozwiązaniem analitycznym.

# 3.1
# W urnie jest 5 kul białych i 2 czarne. Losujemy bez zwracania 3 kule. Jakie jest prawdopodobieństwo, że wszystkie będą białe?
# Rozwiąż to zadanie na "kartce" i numerycznie. Do rozwiązania numerycznego użyj funkcji losuj_z_urny(). 
# Wykonaj losowanie dużą liczbę razy -- powiedzmy 1000 lub 10000 powtórzeń -- zlicz ile razy wypadły trzy kule białe, następnie oblicz częstość.

from random import choice

def losuj_z_urny(liczba_losowań = 1, zwracanie = True, **kule):
    if not zwracanie and liczba_losowań > sum(kule.values()):
        raise ValueError('Liczba losowań bez zwracania większa niż liczba kul.')
    urna = []
    for kula, liczność in kule.items():
        urna.extend(liczność * [kula])
    worek = [] # wylosowane kule
    for _ in range(liczba_losowań):
        kula = choice(urna)
        worek.append(kula)
        if not zwracanie:
            urna.remove(kula)
    return worek
    

N = 10 # liczba doswiadczen losowych
k = 0 # liczba samych bialych

for _ in range(N):
    kule = losuj_z_urny(liczba_losowań = 3, zwracanie = False, b = 5, cz = 2)
    
    if kule == ['b', 'b', 'b']:
        k += 1
        
print(f'Częstość = {k/ N:.4f}')


# 3.2
# Dane są dwie urny: w pierwszej znajdują się dwie kule czarne i jedna biała, w drugiej -- trzy białe. 
# Losujemy urnę (z prawdopodobieństwem 1/2) a następnie losujemy jedną kulę. Jakie jest prawdopodobieństwo, 
# tego że losowaliśmy z pierwszej urny, jeżeli wiadomo, że wylosowana kula jest biała.
# Rozwiąż zadanie dwoma sposobami: tradycyjnie wykorzystując teorię prawdopodobieństwa i numerycznie. 
# W rozwiązaniu numerycznym skorzystaj z funkcji losuj_z_urny().

def eksperyment(n):
    pierwsza_urna = {'Czarna': 2, 'Biała': 1}
    druga_urna = {'Biała': 3}
    licznik = 0  # Licznik trafień do pierwszej urny
    for _ in range(n):
        if choice([True, False]):  # Losowanie urny (True - pierwsza urna, False - druga urna)
            worek = losuj_z_urny(1, True, **pierwsza_urna)
            if 'Biała' in worek:
                licznik += 1
        else:
            worek = losuj_z_urny(1, True, **druga_urna)
            if 'Biała' in worek:
                licznik += 1
    return licznik / n

prawdopodobienstwo = eksperyment(1000000)
print(prawdopodobienstwo)


# 3.3
# Rozpatrujemy doświadczenie losowe jak w punkcie 3.2. Niech U będzie zmienną losową oznaczającą wylosowaną urnę, a K 
# zmienną losową oznaczającą wylosowaną kulę. Napisz program, który korzystając z częstościowej interpretacji prawdopodobieństwa wyznaczy 
# przybliżoną tabelę rozkładu łącznego wektora losowego (U,K). Wykorzystaj wyznaczoną tabelę do ponownego rozwiązania zadania 3.2.

def wyznacz_rozkład_łączny(liczba_doświadczeń):
    urny = ['Pierwsza', 'Druga']
    kule = ['Czarna', 'Biała']
    tabela_rozkładu_łącznego = {}

    for _ in range(liczba_doświadczeń):
        urna = choice(urny)
        kula = choice(kule)
        para = (urna, kula)

        if para in tabela_rozkładu_łącznego:
            tabela_rozkładu_łącznego[para] += 1
        else:
            tabela_rozkładu_łącznego[para] = 1

    for para, liczba_wystąpień in tabela_rozkładu_łącznego.items():
        prawdopodobieństwo = liczba_wystąpień / liczba_doświadczeń
        tabela_rozkładu_łącznego[para] = prawdopodobieństwo

    return tabela_rozkładu_łącznego

def prawdopodobieństwo_zadania_poprzedniego(tabela_rozkładu_łącznego):
    para = ('Pierwsza', 'Biała')
    return tabela_rozkładu_łącznego.get(para, 0)

# Wywołanie funkcji do wyznaczenia tabeli rozkładu łącznego
tabela_rozkładu = wyznacz_rozkład_łączny(1000000)

# Wywołanie funkcji do obliczenia prawdopodobieństwa z zadania poprzedniego
prawdopodobieństwo = prawdopodobieństwo_zadania_poprzedniego(tabela_rozkładu)

print(prawdopodobieństwo)
