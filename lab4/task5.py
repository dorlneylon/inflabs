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

    with open(f"{file.split('.')[0]}_5.csv", "w+") as output:
        for key in d:
            output.write(f"{key},")
        output.seek(output.tell()-1, 0)
        output.truncate()
        output.write("\n")
        for key in d:
            if not isinstance(d[key], list): output.write(f"{d[key]},")
            else:
                for line in d[key]:
                    output.write(f"{line}\n,,")
                output.seek(output.tell() - 3, 0)
                output.truncate()
        

yml_parser("schedule.yml")

