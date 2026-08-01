print("ДОБРО ПОЖАЛОВАТЬ!")
print("Команды: /help, /crypt, /decrypt, /exit")

while True:
    vvod = input().strip()

    if vvod == "":
        continue

    parts = vvod.split(" ", 1)

    komanda = parts[0].lower()

    if len(parts) > 1:
        tekst = parts[1]
    else:
        tekst = ""

    if komanda == "/help":
        print("/crypt текст - зашифровать")
        print("/decrypt текст - расшифровать")
        print("/exit - выход")

    elif komanda == "/exit":
        print("Пока!")
        break

    elif komanda == "/crypt":
        if tekst == "":
            print("Введите текст")
        else:
            rezultat = ""
            for bukva in tekst:
                rezultat = rezultat + chr(ord(bukva) + 3)
            print(rezultat)

    elif komanda == "/decrypt":
        if tekst == "":
            print("Введите текст")
        else:
            rezultat = ""
            for bukva in tekst:
                rezultat = rezultat + chr(ord(bukva) - 3)
            print(rezultat)

    else:
        print("Команда не найдена. Введите /help")