import re

def yml_parser(file: str) -> None:
    with open(file) as inputfile:
        d = {}
        lkey = ""

        while (s := inputfile.readline()):
            s = s.strip()
            
            if not s: continue

            if re.match(r".*:$", s):
                lkey = s[:-1]
                d[lkey.strip()] = []
            elif re.match(r"^-.*", s):
                try:
                    d[lkey] += [{}]
                except:
                    print("Неправильный формат файла"); quit()
            elif lkey:
                key, *string = re.findall(r"^(\w*\s*):\s*(.*)", s)[0]
                try: d[lkey.strip()][-1][key] = ":".join(string).strip()
                except: print("Неправильный формат файла - не задана группа значений."); quit()
            elif ":" in s:
                key, *string = s.split(":")
                d[key.strip()] = ":".join(string).strip()
            else:
                print("Неправильный формат файла"); quit()


    with open(f"{file.split('.')[0]}_3.json", "w+") as output:
        output.write(str(d).replace("'", '"'))

yml_parser("schedule.yml")

