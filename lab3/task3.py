import re

haspayments = {
    "Почему Б.А. Р3000" : 1,
    "Гдеденьги Д. Б. Р3111" : 1,
    "Господибоже А.А. Р3112" : 1,
    "Jesus H.T. Р6666" : 1,
    "Чохз Ч. Х. Р3112" : 99999,
    "Аааа А.А. Р3112" : 100,
    "Кекус ОЧ Р3112" : 1
}

print("BEFORE")

print(*[i for i in haspayments if haspayments[i]], sep="\n")

def checker() -> None:
    for student in haspayments:
        if re.match("[A-ZА-Я]\w+\s+[A-ZА-Я]\.{0,1}\s*[A-ZА-Я]\.{0,1}\sР3112", student):
            haspayments[student] = 0

checker()

print("\nAFTER")

print(*[i for i in haspayments if haspayments[i]], sep="\n")