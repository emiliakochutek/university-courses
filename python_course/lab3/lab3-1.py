# W obu podpunktach tego zadania należy zmienić w miejscu zdefiniowaną niżej listę słowa. 
# Komórkę z definicją listy zatwierdź przed rozpoczęciem każdego podpunktu.

# 1.1
# W liście słowa zamień każde słowo na liczbę tworzących je znaków. Operację wykonaj w miejscu, nazwa słowa ma cały czas wskazywać na ten sam obiekt.

wierszyk = '''czarna krowa w kropki bordo
gryzła trawę kręcąc mordą
kręcąc mordą i rogami
gryzła trawę wraz z jaskrami'''

słowa = wierszyk.split()
_słowa_testref = słowa

for i in range(len(słowa)):
    słowa[i] = len(słowa[i])

assert słowa is _słowa_testref, 'Nie wykonałeś operacji "w miejscu".'
assert słowa[:3] == [6, 5, 1]
assert słowa[-3:] == [4, 1, 8]
assert sum(słowa) == len(wierszyk.replace(' ', '').replace('\n', ''))


# 1.2
# Rozszerz listę słowa o listę słowa, w której odwrócono kolejność. Operację wykonaj w miejscu.

wierszyk = '''czarna krowa w kropki bordo
gryzła trawę kręcąc mordą
kręcąc mordą i rogami
gryzła trawę wraz z jaskrami'''

słowa = wierszyk.split()
_słowa_testref = słowa

słowa.extend(słowa[::-1])

assert słowa is _słowa_testref, 'Nie wykonałeś operacji "w miejscu".'
assert słowa[:3] == ['czarna', 'krowa', 'w']
assert słowa[-3:] == ['w', 'krowa', 'czarna']
