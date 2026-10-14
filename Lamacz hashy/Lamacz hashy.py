import hashlib

program_zakonczony = False

while program_zakonczony == False:
    hash_uzytkownika = input("Prosze podac hash do zlamania: ").lower()

    format_poprawny = False
    while format_poprawny == False:
        format_hasha = input("Jaki format ma ten hash? (md5, sha256): ").lower()
        if format_hasha not in ["md5", "sha256"]:
            print("Nie znaleziono formatu")
        else:
            format_poprawny = True

    plik_poprawny = False
    while plik_poprawny == False:
        nazwa_pliku = input("Prosze podac nazwe pliku z lista hasel do sprawdzenia (np. Hasla.txt): ")
        try:
            with open(f"{nazwa_pliku}", "r") as plik:
                lista_hasel = plik.read().splitlines()
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku. Plik musi znajdowac sie w tym samym folderze co obecnie wlaczony kod!")
            print("Jesli plik znajduje sie gdzies indziej i nie chcesz go przenosic musisz podac pelna sciezke do niego (np. C:/Users/Nazwa/Desktop/Hasla.txt)")
            continue
        if len(lista_hasel) == 0:
            print("W tym pliku nie znajduja sie zadne hasla!")
            continue
        else:
            plik_poprawny = True

    znaleziono = False
    for haslo in lista_hasel:
        if format_hasha == "md5":
            hash_md5 = hashlib.md5(haslo.encode()).hexdigest()
            if hash_md5 == hash_uzytkownika:
                print(f"Znaleziono! Haslo to: {haslo}")
                znaleziono = True
                break
        elif format_hasha == "sha256":
            hash_sha256 = hashlib.sha256(haslo.encode()).hexdigest()
            if hash_sha256 == hash_uzytkownika:
                print(f"Znaleziono! Haslo to: {haslo}")
                znaleziono = True
                break

    if znaleziono == False:
        print("Nie znaleziono takiego hasla!")

    pytanie_zadane = False
    while pytanie_zadane == False:
        odpowiedz_koncowa = input("Czy chcialbys sprawdzic inny hash? (Y/N): ").upper()
        if odpowiedz_koncowa == "Y":
            pytanie_zadane = True
        elif odpowiedz_koncowa == "N":
            pytanie_zadane = True
            program_zakonczony = True
        else:
            print("Zla wartosc!")