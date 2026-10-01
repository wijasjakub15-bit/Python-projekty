import socket
import re

format = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
koniec = False

while not koniec:
    pytanie_adres = False
    while not pytanie_adres:
        pytanie_adres_format = False
        while not pytanie_adres_format:
            print("Podawanie cudzego adresu ip bez jego zgody to naruszenie i moze stanowic naruszenie prawa!")
            adres = input("Prosze podac swoj adres ip(x.x.x.x): ")
            if re.match(format, adres):
                pytanie_adres_format = True
            else:
                print("Niepoprawny format!")

        pytanie_adres_poprawnosc = False
        while not pytanie_adres_poprawnosc:
            adres_poprawnosc = input(f"Czy adres '{adres}' jest poprawny?(Y/N): ").upper()
            if adres_poprawnosc == "Y":
                pytanie_adres = True
                pytanie_adres_poprawnosc = True
            elif adres_poprawnosc == "N":
                pytanie_adres = False
                pytanie_adres_poprawnosc = True
            else:
                print("Niepoprawna wartosc!")

    pytanie_od = False

    while not pytanie_od:
        od = input("Prosze podac od ktorego portu rozpoczac skan(1-65535): ")
        if not od.isdigit():
            print("Niepoprawna wartosc!")
            continue
        od = int(od)
        if od > 65535 or od < 1:
            print("Niepoprawna wartosc!")
            continue
        else:
            pytanie_od = True

    pytanie_do = False

    while not pytanie_do:
        do = input("Prosze podac do ktorego portu skanowac(1-65535): ")
        if not do.isdigit():
            print("Niepoprawna wartosc!")
            continue
        do = int(do)
        if do > 65535 or do < 1:
            print("Niepoprawna wartosc!")
            continue
        elif do < od:
            print("Wartosc ostatniego portu nie moze byc mniejsza badz rowna poczatkowemu portowi!")
        else:
            pytanie_do = True

    otwarte_porty = []

    print("")
    print("Skanuje, to moze zajac czas odpowiedni ilosci portow do przeskanowania, prosze o cierpliwosc")
    print("1 port ≈ 0.5 sekundy")
    print("10 portow ≈ 5 sekund")
    print("100 portow ≈ 50 sekund")
    print("")

    for port in range(od, do+1):
        if port % 10 == 0:
            print("Trwa skanowanie...")
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gniazdo.settimeout(0.5)
        skaner = gniazdo.connect_ex((adres, port))
        if skaner == 0:
            otwarte_porty.append(port)
        gniazdo.close()

    print("")
    if len(otwarte_porty) == 0:
        print("Nie zaleziono zadnych otwartych portow!")
    elif len(otwarte_porty) == 1:
        print(f"Dla adresu ip {adres} z zakresem portow {od} - {do}, znaleziono {len(otwarte_porty)} otwarty port!")
        print(f"{otwarte_porty}")
    elif len(otwarte_porty) >= 2:
        print(f"Dla adresu ip {adres} z zakresem portow {od} - {do}, znaleziono {len(otwarte_porty)} otwarte porty!")
        print(f"{otwarte_porty}")

    pytanie_ponownie = False
    while not pytanie_ponownie:
        pytanie = input("Czy chcialbys przeskanowac inny adres ip?(Y/N): ").upper()
        if pytanie == "Y":
            pytanie_ponownie = True
        elif pytanie == "N":
            pytanie_ponownie = True
            koniec = True
        else:
            print("Niepoprawna wartosc!")