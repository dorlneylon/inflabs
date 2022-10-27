import re

haspayments = {
    "Почему Б.А. Р3000" : 1,
    "Гдеденьги Д. Б. Р3111" : 1,
    "Господибоже П.П. Р3112" : 1,
    "Jesus H.T. Р6666" : 1,
    "Чохз Ч. Х. Р3112" : 99999,
    "Аааа А.А. Р3112" : 100,
    "Кекус ОЧ Р3112" : 1,
    "Рофлан Е Б Р3112" : 1,
    "Лол К.К. Р0000" : 1
}

print("BEFORE")

print(*[i for i in haspayments if haspayments[i]], sep="\n")

def checker() -> None:
    studlist = [student for student in haspayments if re.search(r"[A-ZА-Я]\w+\s+(?:[A-ZА-Я]\.?\s*){2} Р3112", student)]
    
    for stud in studlist:
        a, b = re.findall(r"([А-ЯA-Z])\.?\s*([А-ЯA-Z])\.?\s*", stud)[0]
        if a == b: haspayments[stud] = 0


checker()

print("\nAFTER")

print(*[i for i in haspayments if haspayments[i]], sep="\n")
