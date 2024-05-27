# 1.1
# Napisz funkcję wc(f). Parametr f jest strumieniem tekstu (czyli np. wartością zwróconą przez open() w trybie tekstowym t). 
# Funkcja zwraca krotkę trzech liczb:
#     liczba wierszy definiowana jako liczba znaków nowej linii '\n';
#     liczba słów - słowo to ciągły fragment łańcucha znaków ograniczony białymi znakami lub początkiem/końcem łańcucha;
#     liczba znaków - liczba wszystkich znaków w f.

import sys

# def wc(f):
#     wiersze, slowa, znaki = 0, 0, 0
#     
#     for linia in f:
#         if '\n' in linia:
#             wiersze += 1
#         znaki += len(linia)
#         slowa += len(linia.split())
#     return wiersze, slowa, znaki

def wc(f):
    tekst = f.read()
    wiersze = tekst.count('\n')
    slowa = len(tekst.split())
    znaki = len(tekst)
    return wiersze, slowa, znaki


import io

tekst = ''
with io.StringIO(tekst) as f:
    assert wc(f) == (0, 0, 0)

tekst = '\n\n'
with io.StringIO(tekst) as f:
    assert wc(f) == (2, 0, 2)

tekst = 'ala ma kota'
with io.StringIO(tekst) as f:
    assert wc(f) == (0, 3, 11)
    
tekst = '''ala ma kota
i
psa'''
with io.StringIO(tekst) as f:
    assert wc(f) == (2, 5, 17)
    
tekst = '''ala ma kota
i
psa
'''
with io.StringIO(tekst) as f:
    assert wc(f) == (3, 5, 18)


# 1.2
# Napisz program wc.py. Program powinien wyświetlać liczbę wierszy, słów i znaków w pliku tekstowym dostarczanym jako parametr w wierszu poleceń:
# $ python wc.py lab_I.html                                           
#  13547 31723 295192 lab_I.html
# Na końcu kounikatu program wypisuje nazwę badanego pliku.

if __name__ == '__main__':
    try:
        file_path = sys.argv[1] 
        
        with open(file_path, 'rt', encoding = 'utf8') as f:
            wiersze, slowa, znaki = wc(f)
            print(f' {wiersze} {slowa} {znaki} {file_path} ')
        
    except FileNotFoundError:
        print("Błąd: Podany plik nie istnieje.")
    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu pliku.")
    except:
        print("Błąd: Wystąpił nieoczekiwany błąd podczas przetwarzania pliku.")

# Sprawdzenie, czy podano nazwę pliku jako argument wiersza poleceń
if len(sys.argv) < 2:
    print("Błąd: Podaj nazwę pliku jako argument.")
else:
    filename = sys.argv[1]
    wc(filename)
    
        
# 1.3
# Uogólnienie programu wc.py. Teraz program powinien akceptować jeden lub więcej plików tekstowych z wiersza poleceń. 
# Jeśli plik jest tylko jeden, to działanie programu jest takie samo jak w poprzednim punkcie. Gdy plików jest więcej, to poza wypisaniem statystyk 
# dla poszczególnych plików, powinno pojawić się również zbiorcze podsumowanie:
# $ python wc.py lab_I.html lab_II.html /tmp/a.txt 
#   13547  31723 295192 lab_I.html
#   13576  31631 297762 lab_II.html
#       3      5     18 /tmp/a.txt
#   27126  63359 592972 razem

import sys

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            characters = 0

            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)

            print(f"{lines:7} {words:7} {characters:7} {filename}")

            return lines, words, characters

    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie istnieje.")
    except PermissionError:
        print(f"Błąd: Brak uprawnień do odczytu pliku '{filename}'.")
    except:
        print(f"Błąd: Wystąpił nieoczekiwany błąd podczas przetwarzania pliku '{filename}'.")

def total_summary(results):
    total_lines = sum(lines for lines, _, _ in results)
    total_words = sum(words for _, words, _ in results)
    total_characters = sum(characters for _, _, characters in results)

    print(f"{total_lines:7} {total_words:7} {total_characters:7} razem")

# Sprawdzenie, czy podano nazwy plików jako argumenty wiersza poleceń
if len(sys.argv) < 2:
    print("Błąd: Podaj nazwę przynajmniej jednego pliku jako argument.")
else:
    filenames = sys.argv[1:]

    results = []
    for filename in filenames:
        result = wc(filename)
        if result:
            results.append(result)

    if len(results) > 1:
        print()
        total_summary(results)
