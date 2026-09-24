import hashlib
import requests

koniec = False

while not koniec:
    haslo_uzytkownika = input("Prosze podac swoje haslo do sprawdzenia: ")

    haslo_uzytkownika_bajty = haslo_uzytkownika.encode('utf-8')
    hash_hasla_uzytkownika = hashlib.sha1(haslo_uzytkownika_bajty).hexdigest().upper()

    odpowiedz = requests.get(f"https://api.pwnedpasswords.com/range/{hash_hasla_uzytkownika[:5]}")

    lista = odpowiedz.text.splitlines()

    wycieklo = False

    for linia in lista:
        rozdzielenie = linia.split(":")
        reszta_hasha = rozdzielenie[0]
        ilosc = rozdzielenie[1]
        if reszta_hasha == hash_hasla_uzytkownika[5:]:
            print(f"Twoje haslo wycieklo az {ilosc} razy!")
            wycieklo = True

    if not wycieklo:
        print("Twoje haslo nie wycieklo ani razu!")

    poprawna_odpowiedz = False

    while not poprawna_odpowiedz:
        inne_haslo = input("Czy chcialbys sprawdzic inne haslo?(Y/N): ").upper()
        if inne_haslo == "Y":
            poprawna_odpowiedz = True
        elif inne_haslo == "N":
            poprawna_odpowiedz = True
            koniec = True
        else:
            print("Prosze podac poprawna odpowiedz!")