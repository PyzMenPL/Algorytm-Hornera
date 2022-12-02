###
# Dzielenie
###

def horner(user_input):
    print(user_input)
    # Pozbądź wpis użytkownika wszystkiego, co niepotrzebne
    # Pozbądź się spacji
    user_input = list(user_input.strip().lower())

    while ' ' in user_input:
        del user_input[user_input.index(' ')]

    # Dodatkowo: Sprawdź scenariusz, w którym będzie więcej niż jedna niewiadoma w user_input

    # Znajdź index miejsca, w którym znajduje się : lub /
    division_index = int
    if ':' in user_input or '/' in user_input:
        division_index = user_input.index(':') if ':' in user_input else user_input.index('/')
        # Code above works the same as:
        """
        division_index = int
        if ':' in user_input:
            division_index = user_input.index(':')
        else:
            division_index = user_input.index('/')
        """
    else:
        print("Nie znaleziono znaku dzielenia")
        return

    divider = user_input[division_index]
    dzielna = user_input[:division_index]
    dzielnik = user_input[-(len(user_input) - division_index - 1):]

    ## Dzielnik i dzielna muszą być w nawiasach
    # W sumie to nawias nie musi się zawsze pojawić,
    # Jeżeli chciałbym Hornerem podzielić 2x^3 i x
    # to chyba nic nie stoi mi na przeszkodzie
    ##
    ## Dzielnik musi być w postaci (coś x +/- coś tam) i gdy nie ma x do potęgi
    # Sprawdzamy, czy w dzielniku jest 'x', '+' lub '-' i nie ma '^'
    if not (('x' in dzielnik) and (('+' in dzielnik) or ('-' in dzielnik)) and ('^' not in dzielnik)):
        print("Zła składnia dzielnika")
        return

    # Sprawdź, czy można wykorzystać algorytm

    # Dodatkowo: Sprawdź, czy można przekształcić dzielnik
    # tak, aby dało się zastosować algorytm

    # Wydobądź z user_input to, czego potrzebujesz:
    # Współczynniki, stopnie współczynników i liczbę, przez którą będziesz mnożył

    ## Stopnie
    ### Najpierw pozyskujemy wszystkie stopnie
    ### (ponieważ mogą nie być w poprawnie matematycznej kolejności)
    stopnie = {}
    for znak in range(0, len(dzielna)):
        if dzielna[znak] == '^':
            znak_org = znak
            znak += 1
            stopien = dzielna[znak]
            znak += 1
            while dzielna[znak].isdigit():
                stopien += dzielna[znak]
                znak += 1

            # znak_org -> ^
            # znak_org - 1 -> x
            # znak_org - 2 -> liczba
            znak = znak_org - 2
            wartosc = ''
            while dzielna[znak].isdigit():
                wartosc += dzielna[znak]
                znak -= 1
            stopnie[int(stopien)] = wartosc

    ### Zostawiamy największy współczynnik
    max_wspolczynnik = max(stopnie.keys())

    ### Uzupełniamy brakujące stopnie zerami
    stopnie_cp = {}
    for i in range(0, max_wspolczynnik + 1):
        try:
            if stopnie[i] != 0:
                stopnie_cp[i] = stopnie[i]
        except KeyError:
            stopnie_cp[i] = 0

    stopnie = stopnie_cp

    ### Musimy jeszcze sprawdzić pierwszy i zerowy stopień

    # Dzielna od końca
    # pierwszy element nawias
    dzielna_cp = list(reversed(dzielna[:]))
    del dzielna_cp[0]
    # liczba dla stopnia zerowego
    # znak i x
    # liczba dla stopnia pierwszego

    pierwsza = True

    zero = 0
    jeden = 0

    for znak in range(0, len(dzielna_cp) + 1):
        wartosc = ''
        while dzielna_cp[znak].isdigit():
            wartosc += dzielna_cp[znak]
            znak += 1

        zero = wartosc
        break

    # Usuwam tyle jaką długość na zmienna zero oraz usuwa znak i x
    for i in range(0, len(zero) + 2):
        del dzielna_cp[0]

    jeden = dzielna_cp[0] if dzielna_cp[0].isdigit() else 0

    stopnie[0] = zero
    stopnie[1] = jeden

    print(stopnie)

    ## Liczba do mnożenia

    # Zaimplementuj algorytm

    # W graficzny sposób przedstaw odpowiedź, a potem wyświetl wzór


###
# Obliczanie konkretnej wartości
###

# Wyświetl instrukcję (co to wzór Hornera i jak z niego korzystać)

print("Wybierz czy chcesz podzielić wielomian czy obliczyć jego wartość dla konkretnego x")

# print("Wypisz działanie:")
# user_input = input('w(x)=')

horner('(4x^2+2)(x+5)')
horner('(4x^6):(x^2+6)')
horner('(2x^3+4x-7)/(x-2)')
horner('(2x^12+4x^3-7)/(x-2)')
