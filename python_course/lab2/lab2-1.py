# Napisz program, który pobiera od użytkownika (jednym poleceniem input()) ciąg liczb całkowitych rozdzielonych spacjami lub tabami (dowolną ilością).
# Program ma wyświetlać sumę i średnią arytmetyczną tego ciągu (ile wynosi średnia arytmetyczna ciągu pustego?!).
# Program powinien wymuszać wprowadzenie danych w poprawnym formacie: po podaniu niepoprawnych danych program ponownie żąda ich wprowadzenia.
# Wykorzystaj instrukcję try. Łańcuch znaków przetwórz metodą łańcuchów .split() i funkcją int().

while True:
    try:
        ciag = input("Podaj ciąg liczb całkowitych rozdzielonych spacjami lub tabami: ").split()
        suma = 0
        licznik = 0
        for element in ciag:
            suma += int(element)
            licznik += 1
        print(f"Suma: {suma}")
        print(f"Średnia: {suma / licznik}")
    except ZeroDivisionError:
        print("Podano ciąg pusty")
    except ValueError:
        print("Podano niepoprawny format")


# Zmień program z punktu 1.1 tak, aby dawał użytkownikowi trzy szanse na wprowadzenie prawidłowych danych
# później program kończy działanie stosownym komunikatem.

szanse = 3

while szanse > 0:
    try:
        ciag = input("Podaj ciąg liczb całkowitych rozdzielonych spacjami lub tabami: ").split()
        suma = 0
        licznik = 0
        for element in ciag:
            suma += int(element)
            licznik += 1
        print(f"Suma: {suma}")
        print(f"Średnia arytmetyczna: {suma / licznik}")
        break
    except ZeroDivisionError:
        print("Podano ciąg pusty")
    except ValueError:
        print("Podano niepoprawny format")
        szanse -= 1

if szanse == 0:
    print("Przekroczono limit prób.")
