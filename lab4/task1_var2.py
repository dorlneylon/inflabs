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
                
                s = s[1:].strip()

                if ":" in s:
                    key, *string = s.split(":")
                    d[lkey][-1][key.strip()] = ":".join(string).strip()
            
            elif lkey:
                key, *string = s.split(":")
                try: d[lkey.strip()][-1][key] = ":".join(string).strip()
                except: print("Неправильный формат файла - не задана группа значений."); quit()
            
            elif ":" in s:
                key, *string = s.split(":")
                d[key.strip()] = ":".join(string).strip()
            
            else:
                print("Неправильный формат файла"); quit()


    with open(f"{file.split('.')[0]}_1.json", "w+") as output:
        
        s = "{\n"
        for key, value in d.items():
            s += f"    \"{key}\": "
            if isinstance(value, list):
                s += "[\n"
                for i in value:
                    s += "        {\n"
                    for k, v in i.items():
                        s += f"            \"{k}\": \"{v}\",\n"
                    s = s[:-2] + "\n"
                    s += "        },\n"
                s = s[:-2] + "\n"
                s += "    ]\n"
            else:
                s += f"\"{value}\",\n"
        s += "}"

        output.write(s)

yml_parser("schedule.yml")

