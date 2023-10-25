# Niech p, q będą dodatnimi liczbami całkowitymi. Napisz program, który wyznaczy liczbę całkowitą x
# spełniającą równość x3+px=q lub stwierdzi, że takiej liczby nie ma.

def find_integer(p, q):
    for x in range(-q, q+1):
        if x**3 + p*x == q:
            return x
    return None

p = int(input("Podaj wartość p: "))
q = int(input("Podaj wartość q: "))

result = find_integer(p, q)

if result is not None:
    print(f"Liczba x spełniająca równość to: {result}")
else:
    print("Nie istnieje liczba x spełniająca równość.")
