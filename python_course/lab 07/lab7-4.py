# Napisz funkcję maks_fragment(seq, f). Parametry
#     f - jednoargumentowa funkcja akceptująca sekwencje, zwracająca True, False. 
#     Zakładamy, że f() jest True na sekwencji pustej i na każdej podsekwencji 
#     s' każdej sekwencji s dla której f(s) jest True.
#     seq - dowolna sekwencja.
# Funkcja zwraca pierwszy od lewej wycinek sekwencji seq, dla którego f() ma wartość True i który ma maksymalną długość.
# Wykorzystaj maks_fragment() w kodzie funkcji znajdującej w dowolnej sekwencji liczb najdłuższy fragment będący ciągiem arytmetycznym.

def maks_fragment(seq, f):
    max_fragment = None
    max_length = 0

    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            if f(seq[i:j]) and j - i > max_length:
                max_fragment = seq[i:j]
                max_length = j - i

    return max_fragment

def najdłuższy_ciąg_arytmetyczny(seq):
    def is_ciąg_arytmetyczny(subseq):
        if len(subseq) < 3:
            return True

        diff = subseq[1] - subseq[0]

        for i in range(2, len(subseq)):
            if subseq[i] - subseq[i - 1] != diff:
                return False
            
        return True

    return maks_fragment(seq, is_ciąg_arytmetyczny)


# Przykładowe użycie
sequence = [1, 2, 3, 5, 8, 13, 14, 15, 18, 20, 22]
result = najdłuższy_ciąg_arytmetyczny(sequence)
print(result)
