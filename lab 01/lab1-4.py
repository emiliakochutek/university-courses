# Napisz program, który wyświetli najmniejszą liczbę n, dla której
# 1+1/2+1/3+⋯+1/n⩾10

n = 1
suma = 0

while suma < 10:
    suma += 1/n
    n += 1

print(n)