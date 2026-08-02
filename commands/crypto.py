def crypt(tekst):
    rezultat = ""

    for bukva in tekst:
        rezultat = rezultat + chr(ord(bukva) + 3)

    return rezultat


def decrypt(tekst):
    rezultat = ""

    for bukva in tekst:
        rezultat = rezultat + chr(ord(bukva) - 3)

    return rezultat