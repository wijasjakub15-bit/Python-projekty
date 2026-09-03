import random
import string

baza_znakow = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*"
dziala = False

while dziala == False:
    haslo = ""

    haslo_inp = input("Podaj dlugosc hasla(8-30): ")

    if haslo_inp.isdigit() == False:
        continue

    haslo_inp = int(haslo_inp)

    if haslo_inp > 30 or haslo_inp < 8:
        print("Zla dlugosc hasla!")
        continue

    for i in range(haslo_inp):
        losowy_znak = random.choice(baza_znakow)
        haslo += losowy_znak

    dziala = True

print(f"Twoje haslo to {haslo}")




