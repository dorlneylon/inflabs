import re

def yml_parser(file: str) -> None:
    with open(file) as inputfile:
        d = {}
        lkey = ""

        while (s := inputfile.readline().strip()):
            if re.match("^\s*-.*", s):
                d[lkey] += [re.findall("^\s*-\s*(.*)", s)[0]]
            elif re.match("^.*:\s*$", s):
                lkey = s
                d[lkey] = []
            else:
                key, data = re.findall("^(.*): (.*)", s)[0]
                d[key] = data

    with open(f"{file.split('.')[0]}_3.json", "w+") as output:
        output.write(str(d))

yml_parser("schedule.yml")

