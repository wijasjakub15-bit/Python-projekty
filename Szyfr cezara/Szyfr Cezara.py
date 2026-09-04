import string

koniec = False

while koniec == False:
    wynik = ""
    poprawnosc = False
    pytanie = False

    tekst = input("Podaj tekst do zaszyfrowania: ")

    while poprawnosc == False:
        przesuniecie = input("Podaj wartosc przesuniecia(1-26): ")
        if przesuniecie.isdigit() == False:
            print("Wartosc przesuniecie musi byc cyfra!")
            continue

        przesuniecie = int(przesuniecie)

        if przesuniecie not in range(1,27):
            print("Wartosc przesuniecia musi byc w zakresie 1-26!")
            continue

        poprawnosc = True

    for znak in tekst:
        if znak in string.ascii_uppercase:
            numer_znaku = ord(znak) - 65
            znak_modulo = (numer_znaku + przesuniecie) % 26
            znak_koncowy = chr(znak_modulo + 65)
            wynik += znak_koncowy

        elif znak in string.ascii_lowercase:
            numer_znaku = ord(znak) - 97
            znak_modulo = (numer_znaku + przesuniecie) % 26
            znak_koncowy = chr(znak_modulo + 97)
            wynik += znak_koncowy

        else:
            wynik += znak

    print(f"Twoja zaszyfrowana wiadomosc to - {wynik}")
    print()

    while pytanie == False:
        odpowiedz = input("Czy chcialbys zaszyfrowac kolejna wiadomosc?(T/N): ").upper()
        if odpowiedz not in ["T", "N"]:
            print("Niepoprawna wartosc!")
            continue

        if odpowiedz == "T":
            pytanie = True

        else:
            pytanie = True
            koniec = True