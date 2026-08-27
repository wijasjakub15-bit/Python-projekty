
wszystko = False

while wszystko == False:
    wielka_litera = False
    mala_litera = False
    cyfra = False
    znak_specjalny = False

    haslo = input("Podaj swoje haslo: ")

    if len(haslo) < 8:
        print("Twoje haslo jest za krotkie!")
        continue

    for znak in haslo:
        if znak.isupper():
            wielka_litera = True

        if znak.islower():
            mala_litera = True

        if znak.isdigit():
            cyfra = True

        if znak in ["!", "@", "#", "$", "%", "^", "&", "*"]:
            znak_specjalny = True

    if wielka_litera and mala_litera and cyfra and znak_specjalny:
            wszystko = True
    else:
        print("Twoje haslo nie spelnia wszystkich wymagan!")

print("Twoje haslo jest silne!")


