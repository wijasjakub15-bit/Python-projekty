with open("logi.txt", "r") as logi:
    zawartosc = logi.readlines()

adresy_godziny = {}

for linia in zawartosc:
    rozdzielenie = linia.split(",")
    adres_ip = rozdzielenie[0]
    godzina = rozdzielenie[1].strip()
    if adres_ip not in adresy_godziny:
        adresy_godziny[adres_ip] = [godzina]
    else:
        adresy_godziny[adres_ip].append(godzina)

koniec = False

while not koniec:
    poprawny_limit = False
    while not poprawny_limit:
        limit = input("Prosze podac bezpieczny limit logow dla jednego adresu ip: ")
        if not limit.isdigit():
            print("Prosze podac cyfre!")
        else:
            limit = int(limit)
            poprawny_limit = True

    znaleziono_zagrozenie = False

    for adres in adresy_godziny:
        if len(adresy_godziny[adres]) > limit:
            pierwsza_godzina = adresy_godziny[adres][0]
            ostatnia_godzina = adresy_godziny[adres][-1]
            print(f"Adres ip {adres} moze stanowic zagrozenie! Pierwsza proba {pierwsza_godzina}, ostatnia proba {ostatnia_godzina}")
            znaleziono_zagrozenie = True

    if not znaleziono_zagrozenie:
        print("Zaden adres ip nie stanowi zagrozenia")

    poprawna_odpowiedz = False

    while not poprawna_odpowiedz:
        odpowiedz = input("Czy chcialbys ustawic inny prog limitu bezpieczenstwa?(Y/N): ").upper()
        if odpowiedz == "Y":
            poprawna_odpowiedz = True
        elif odpowiedz == "N":
            koniec = True
            poprawna_odpowiedz = True
        else:
            print("Prosze podac poprawna odpowiedz!")