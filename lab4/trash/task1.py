def yml_parser(file: str) -> None:
    with open(file) as inputfile:
        d = {}
        lkey = ""

        while (s := inputfile.readline()):
            s = s.strip()

            if s[0] == "-":
                d[lkey] += [s[2:]]
            elif s[-1] == ":":
                lkey = s[:-1]
                d[lkey] = []
            else:
                lkey = ""
                k = s.split(":")
                d[k[0]] = k[1][1:]

    with open(f"{file.split('.')[0]}_1.json", "w+") as output:
        output.write(str(d))

yml_parser("schedule.yml")
