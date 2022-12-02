print("Wybierz czy chcesz podzielić czy co inneo (zapomniałem)")
###
# Dzielenie
###

# Wyświetl instrukcję (co to wzór hornera i jak z niego korzystać)

print("Wypisz działanie:")
user_input = input('w(x)=')

def horner(user_input):
    # Ustandarduj wpis użytkownika
    # Pozbądź się spacji
    user_input = list(user_input.strip())
    # 1 Opcja
    '''for znak in user_input[:]:
        if znak == ' ':
            user_input[user_input.index(' ')] = '''
    # 2 Opcja
    while ' ' in user_input:
        del user_input[user_input.index(' ')]

    # Dowiedz się jaką niewiadomą wpisał użytkownik
    # (nie zwracaj uwagi na w(x)= w dosłownie jednej z pierwszych linijek kodu XDDDD)
    '''niewiadoma = str
    for znak in'''

    # Dodatkowo: Sprawdź scenariusz w którym będzie więcej niż jedna niewiadoma w user_input


    # Znajdź index miejsca w którym znajduje się : lub /
    division_index = user_input.index(':') if ':' in user_input else user_input.index('/')
    """
    division_index = int
    if ':' in user_input:
        division_index = user_input.index(':')
    else:
        division_index = user_input.index('/')
    """


    # Sprawdzenie składnię
    ## Musi się pojawić znak dzielenia i niewiadoma (nie koniecznie x)
    if (':' not in user_input) or
    ## Dzielnik i dzielna muszą być w nawiasach
    # W sumie to nawias nie musi się zawsze pojawić
    # Jeżei chciałbym hornerem podzielić 2x^3 i x
    # to chyba nic nie stoi mi na przeszkodzie
    ##
    ## Dzielnik musi być w postaci (coś x +/- coś tam)
    ()

    # Sprawdź czy można wykożystać algorytm

    # Dodatkowo: Sprawdź czy można przekształcić dzielnik (to drugie)
    # tak aby dało się zastosować algorytm

    # Wydobądź z user_input to czego potrzebujesz:
    # Współczynników, stopnie współczynników i liczbę, przez którą będziesz mnożył

    # Zaimplementuj algorytm

    # W graficzny sposób przedstaw odpowiedź, a potem wyświetl wzór

###
# Co innego
###
