import yaml, json

def yml_parser(file: str) -> None:
    with open(file, 'r') as inputstream:
        try:
            tempdict = yaml.safe_load(inputstream)
        except yaml.YAMLError as exc:
            tempdict = {}

    with open(f"{file.split('.')[0]}_2.json", "w", encoding="utf-8") as output:
        json.dump(tempdict, output, ensure_ascii=False, indent=4)

yml_parser("schedule.yml")
