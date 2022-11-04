import re

tests = [
    "Так Гриффит Б.Б. предал друзей и стал апостолом - демоном или богом.",
    "Ты меня переиграл, но я переиграл твоё переигрывание, Штрохейм А. Т.",
    "Карпов Д. В. лично меня отчислит. А Пастор А.В. закроет крышку гроба моего.",
    "Гатс МС, как дела?",
    "Аахаха б.б., дурак."
]

def checker(string: str) -> None:
    (val := re.findall(r"([A-ZА-Я]\w+)\s+(?:[A-ZА-Я]\.?\s*){2}", string)) and print(*val, sep="\n", end="\n\n")

for test in tests:
    print(test)
    checker(test)

def test():
    try:
        w = int(input("\nВы хотите ввести свой тест? Введите 1 или 0.\n"))
        if w not in (0,1): raise Exception
    except:
        print("Повторите попытку")
        test()
        return

    return checker(input("Введите тест:\n")) if w else None

test()