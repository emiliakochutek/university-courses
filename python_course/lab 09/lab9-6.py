# W grze w świnię biorą udział dwie osoby, jedynym potrzebnym rekwizytem 
# są dwie zwykłe kości do gry. Gracz podczas ruchu rzuca obiema kościami naraz i sumuje wyniki, 
# rzuty wykonuje aż do decyzji o wstrzymaniu swojej kolejki albo do momentu, gdy na jednej z kości 
# wypadnie jedynka. Po wstrzymaniu kolejki suma uzyskanych oczek dodawana jest do punktów gracza. 
# Jeśli wypadnie jedynka, to gracz nie zdobywa żadnych punktów. Gracze grają na przemian. 
# Wygrywa ten, który jako pierwszy uzyska 100 lub więcej punktów.

# Alicja i Piotr prowadzą grę w świnię. Alicja zaczyna. Strategia Alicji polega na tym, 
# aby zawsze rzucać dwa razy, a strategia Piotra, aby zawsze rzucać trzy razy. 

# Napisz wywołujące się nawzajem funkcje alicja(konto_alicji, konto_piotra), 
# piotr(konto_piotra, konto_alicji) symulujące przebieg rozgrywki. 
# Zmienne konto_* przechowują aktualny stan konta obojga graczy. 

# Wywołanie alicja(konto_alicji, konto_piotra) odpowiada zagraniu Alicji i wykonuje następujące akcje:
#     sprawdza stan konta Piotra; jeśli jest >= 100, to Piotr wygrał, funkcja jest opuszczana z odpowiednim komunikatem; w przeciwnym razie
#     wykonuje serię rzutów Alicji i aktualizuje jej konto;
#     wywołuje piotr(konto_piotra, konto_alicji).

# Wywołanie piotr(konto_piotra, konto_alicji) ma analogiczny przebieg.

from random import randint

def alicja(konto_alicji = 0, konto_piotra = 0):
    if konto_piotra >= 100:
        print("Piotr wygrał")
    else:
        for rzut in range(2):
            rzut = randint(1, 6)
            if rzut == 1:
                break
            konto_alicji += rzut
        piotr(konto_piotra, konto_alicji)

def piotr(konto_piotra, konto_alicji):
    if konto_alicji >= 100:
        print("Alicja wygrała")
    else:
        for rzut in range(3):
            rzut = randint(1, 6)
            if rzut == 1:
                break
            konto_piotra += rzut
        alicja(konto_alicji, konto_piotra)

alicja()


