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

def checker() -> None:
    print("BEFORE")
    print(*[i for i in haspayments if haspayments[i]], sep="\n")


    studlist = [student for student in haspayments if re.search(r"[A-ZА-Я]\w+\s+(?:[A-ZА-Я]\.?\s*){2} [РP]3112", student)]
    
    for stud in studlist:
        a, b = re.findall(r"([А-ЯA-Z])\.?\s*([А-ЯA-Z])\.?\s*", stud)[0]
        if a == b: haspayments[stud] = 0

    print("\nAFTER")
    print(*[i for i in haspayments if haspayments[i]], sep="\n")


checker()



def test():
    global haspayments

    try:
        w = int(input("\nВы хотите ввести свой тест? Введите количество участников теста или 0, если не хотите делать тест.\n"))
    except:
        print("Повторите попытку")
        test()
        return

    print("Введите участников в формате Фамилия И. О. Г0...0")
    haspayments = {}

    def getter():
        try:
            name = re.findall(r"([A-ZА-Я]\w+\s+(?:[A-ZА-Я]\.?\s*){2}\s+[A-ZА-Я]\d+)", input())[0]
            haspayments[name] = 1
        except:
            print("Соблюдайте формат. Попробуйте еще раз.")
            getter()
            return

    for i in range(w):
        getter()

    checker()

test()