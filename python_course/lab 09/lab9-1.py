# Napisz rekurencyjną funkcję obliczającą maksimum sekwencji przekazywanej jako argument. 
# Funkcję napisz w dwóch wersjach: w postaci rekurencji, która wymaga zapamiętywania 
# odkładanych operacji i w takiej, która umożliwia optymalizację ogonową. W tym pierwszym 
# przypadku jedyny wymagany argument to sama sekwencja, w tym drugim funkcja może wymagać 
# dodatkowych argumentów przechowujących stan wywołania. W obu przypadkach rozpisz 
# wywołanie dla małej przykładowej wartości.

def maksimum(seq):
    if not seq:
        raise ValueError('sekwencja pusta')
    if len(seq) == 1:
        return seq[0]
    a, *seq = seq
    b = maksimum(seq)
    return a if a > b else b

# def maks(seq):
#     mx = seq[0]
#     for _ in seq[1:]:
#         if _ > mx:
#             mx = _
#     return mx 

# ## ogonowa:
# def maks(seq):
#     if not seq:
#         raise ValueError('sekwencja pusta')
#     def maks_tail(seq, mx):
#         if not seq:
#             return mx
#         a, *seq = seq
#         return maks_tail(seq, a if a > mx else mx)
#     return maks_tail(seq, seq[0])

