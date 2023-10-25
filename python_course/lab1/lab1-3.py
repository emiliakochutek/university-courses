# Napisz program, który pobiera od użytkownika dodatnią liczbę całkowitą `n`. Następnie dla liczb od `1` do `n` program wyświetla:

#  * `FizzBuzz`, jeśli liczba jest podzielna przez `3` i `5`;
#  * `Fizz`, jeśli liczba jest podzielna przez `3`;
#  * `Buzz`, jeśli liczba jest podzielna przez `5`;
#  * liczbę, jeśli liczba nie jest podzielna przez `3` ani przez `5`.

n = int(input('podaj dodatnią liczbę całkowitą: '))
if n < 0 or type(n) != int:
    raise ValueError('zle n')
for _ in range(1, n+1):
    if _%3==0 and _%5==0:
        print('FizzBuzz')
    elif _%3==0:
        print('Fizz')
    elif _%5==0:
        print('Buzz')
    else:
        print(_)
