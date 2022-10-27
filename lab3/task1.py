import re

eyes = {
    0 : "",
    1 : ";",
    2 : "X",
    3 : "8",
    4 : "=",
    5 : "["
}

nose = {
    0 : "-",
    1 : "<",
    2 : "-{",
    3 : "<{"
}

mouth = {
    0 : "(",
    1 : ")",
    2 : "O",
    3 : "|",
    4 : "\\",
    5 : "/",
    6 : "P"
}

isu = 368853
var = f"{isu%6}{isu%4}{isu%7}"
smile = f"{eyes[isu%6]}{nose[isu%4]}{mouth[isu&7]}"

print(f"Вариант {var}")

tests = [
    f"I. HATE. EVERYTHING ABOUT YOU. {smile} {smile}",
    f"We're killing strangeeers, we're killing strangeeeers {smile}",
    f"all my friends are toxic {smile}, all ambitionless {smile}, so rude {smile} and always {smile} negative.",
    "Have you and JoJo kissed yet? Not yet, right? Your first kiss is not his! It was me, Dio!",
    f"In this world, is the destiny of mankind controlled by some transcendental entity or law? {smile} Is it like the hand of God hovering above? {smile} At least it is true that man has no control, even over his own will. {smile}"
]

def check_matches(string: str) -> int:
    return len(re.findall(f"{smile}", string))

def checker(string):
    print(f"INPUT: {string}\nNUMBER OF SMILES: {check_matches(string)}")

for i in tests: checker(i)
