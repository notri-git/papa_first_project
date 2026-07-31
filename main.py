print("ДОБРО ПОЖАЛОВАТЬ!")
print("Команды: /help, /crypt, /decrypt, /exit")

while True:
    vvod = input()

    if vvod == "":
        continue

    if vvod == "/help":
        print("/crypt текст - зашифровать")
        print("/decrypt текст - расшифровать")
        print("/exit - выход")

    elif vvod == "/exit":
        print("Пока!")
        break

    else:
        komanda = ""
        tekst = ""
        probel_nayden = False

        for bukva in vvod:
            if bukva == " " and not probel_nayden:
                probel_nayden = True
            elif not probel_nayden:
                komanda = komanda + bukva
            else:
                tekst = tekst + bukva

        komanda = komanda.lower()

        if komanda == "/crypt":
            rezultat = ""
            for bukva in tekst:
                rezultat = rezultat + chr(ord(bukva) + 3)
            print(rezultat)

        elif komanda == "/decrypt":
            rezultat = ""
            for bukva in tekst:
                rezultat = rezultat + chr(ord(bukva) - 3)
            print(rezultat)

        else:
            print("Команда не найдена. Введите /help")