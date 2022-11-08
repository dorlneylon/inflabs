import csv

def yml_parser(file: str) -> None:
    with open(file) as inputfile:
        d = {}
        lkey = ""

        while (s := inputfile.readline()):
            s = s.strip()

            if not s: continue

            if s[-1] == ":":
                lkey = s[:-1]
                d[lkey.strip()] = []
            elif s[0] == "-":
                try:
                    d[lkey] += [{}]
                except:
                    print("Неправильный формат файла"); quit()
            elif lkey:
                key, *string = s.split(":")
                try: d[lkey.strip()][-1][key] = ":".join(string).strip()
                except: print("Неправильный формат файла - не задана группа значений."); quit()
            elif ":" in s:
                key, *string = s.split(":")
                d[key.strip()] = ":".join(string).strip()
            else:
                print("Неправильный формат файла"); quit()



    headstr = ",".join(key for key in d)
    headstr += "\n"
    headstr += ",".join(d[key] for key in d if isinstance(d[key], str))
    lstr = ""
    c = 0
    for lesson in d["lessons"]:
        c += 1
        lstr += f"\nlesson №{c}\n"
        for char in lesson:
            lstr += f",,{char},{lesson[char].replace(', ', '; ')}\n"

    with open('schedule_5.csv', 'w') as csvstream:
        csvstream.writelines([headstr,lstr])
        

yml_parser("schedule.yml")

