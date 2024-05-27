# Celem tego zadania jest napisanie funkcji sortującej według algorytmu sortowania przez scalanie.

# 5.1
# Napisz funkcję scal(A, p, q, r). Parametr A jest listą, wartości p, q, r to liczby całkowite grające role indeksów. 
# Zakładamy, że   0 <= p <= q <= r <= len(A)  oraz, że listy A[p:q], A[q:r] są już posortowane niemalejąco. 
# Funkcja przepisuje wartości z obu wycinków do fragmentu A odpowiadajacego A[p:r] w taki sposób, 
# aby fragment ten był posortowany niemalejąco. Funkcja działa w miejscu, nic nie zwraca. 
# Uprość sobie przepisywanie tworząc dwie nowe listy przechowujące fragmenty A[p:q] i A[q:r].

def scal(A, p, q, r):
    left_part = A[p:q]
    right_part = A[q:r]
    i, j, k = 0, 0, p
    # i - indeks w left_part,   j - indeks w right_part
    # k - indeks w A[p:r]
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            A[k] = left_part[i]
            i += 1
        else:
            A[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        A[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        A[k] = right_part[j]
        j += 1
        k += 1



A = [3, 4, 5, 6]
scal(A, 0, 2, 4)
assert A == [3, 4, 5, 6]

A = [5, 6, 1, 2, 3, 4]
scal(A, 0, 2, 6)
assert A == [1, 2, 3, 4, 5, 6]

A = [100, 200, 150, 5, 6, 1, 2, 3, 4, -5, -7]
scal(A, 3, 5, 9)
assert A == [100, 200, 150, 1, 2, 3, 4, 5, 6, -5, -7]


# 5.2
# Napisz funkcję sortuj_przez_scalanie(A, p, r). Parametr A jest listą, parametry p i r grają role indeksów. 
# Wywołanie sortuj_przez_scalanie(A, p, r) sortuje niemalejąco w miejscu fragment A odpowiadający A[p:r]. Wykorzystaj algorytm:
#     jeśli r - p < 2, to fragment jest już posortowany, można opuścić funkcję; w przeciwnym razie
#     wywołaj sortuj_przez_scalanie(A, p, q) i sortuj_przez_scalanie(A, q, r), gdzie q jest indeksem w połowie między p i r.
#     wywołaj scal(A, p, q, r).

def sortuj_przez_scalanie(A, p, r):
    if (r - p) < 2:
        return
    q = (p + r) // 2
    sortuj_przez_scalanie(A, p, q)
    sortuj_przez_scalanie(A, q, r)
    scal(A, p, q, r)

def sortuj(A):
    sortuj_przez_scalanie(A, 0, len(A))
    
A = []
sortuj(A)
assert A == []

A = [1]
sortuj(A)
assert A == [1]

A = [4, 3, 2]
sortuj(A)
assert A == [2, 3, 4]

A = [2, 1, 2, -2]
sortuj(A)
assert A == [-2, 1, 2, 2]

A = list(range(1000, 0, -1))
sortuj(A)
A = list(range(1, 1001))