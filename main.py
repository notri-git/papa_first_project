from commands.crypto import crypt
from commands.crypto import decrypt

from commands.system import os_info
from commands.system import hostname
from commands.system import pwd
from commands.system import ls
from commands.system import dt

from commands.weather import weather

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
        print("/os - информация о системе")
        print("/hostname - имя компьютера")
        print("/pwd - текущая папка")
        print("/ls - список файлов")
        print("/dt - дата и время")
        print("/weather город - узнать погоду")
        print("/exit - выход")

    elif komanda == "/exit":
        print("Пока!")
        break

    elif komanda == "/crypt":
        if tekst == "":
            print("Введите текст")
        else:
            print(crypt(tekst))
    elif komanda == "/os":
        os_info()

    elif komanda == "/hostname":
        hostname()

    elif komanda == "/pwd":
        pwd()

    elif komanda == "/ls":
        ls()

    elif komanda == "/dt":
        dt()

    elif komanda == "/weather":
        if tekst == "":
            print("Введите город")
        else:
            weather(tekst)

    elif komanda == "/decrypt":
        if tekst == "":
            print("Введите текст")
        else:
            print(decrypt(tekst))

    else:
        print("Команда не найдена. Введите /help")