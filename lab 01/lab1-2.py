# Napisz program wyświetlający tabliczkę mnożenia dla zadanej wartości 1⩽n⩽15. Liczbę n wprowadza użytkownik.

# Przykład dla n=9:

# 1   2   3   4   5   6   7   8   9   
# 2   4   6   8   10  12  14  16  18  
# 3   6   9   12  15  18  21  24  27  
# 4   8   12  16  20  24  28  32  36  
# 5   10  15  20  25  30  35  40  45  
# 6   12  18  24  30  36  42  48  54  
# 7   14  21  28  35  42  49  56  63  
# 8   16  24  32  40  48  56  64  72  
# 9   18  27  36  45  54  63  72  81

# W programie wykorzystaj formatowanie łańcuchów (metoda str.format() lub f-strings).




# Rozwiązanie #1
n = int(input('Podaj n: '))
for a in range(1, n+1):
   for b in range(1, n+1):
      print(f'{a * b:<4}', end=' ')
   print()


# Rozwiązanie #2a
n = int(input('Podaj n: '))
l = []
for i in range(1, n+1):
    for j in range(1, n+1):
        l.append(i*j)
counter = 0
for i in l:
    print("{0:3d}".format(i), end=" ")
    counter += 1
    if counter%n==0:
        counter = 0
        print("\n")


# Rozwiązanie #2b
n = int(input('Podaj n: '))
l = [i*j for i in range(1, n+1) for j in range(1, n+1)]
counter = 0
for i in l:
    print("{0:3d}".format(i), end=" ")
    counter += 1
    if counter%n==0:
        counter = 0
        print("\n")