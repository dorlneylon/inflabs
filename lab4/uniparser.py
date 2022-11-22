class YamlParser:
    @classmethod
    def vp(cls, v: [str, int, bool, float]) -> [str, int, bool, float, dict, list]:
        return int(v) if v.isnumeric() else float(v) if "." in v else [] if v=="[]" else {} if v=="{}" else v[1:-1] if v[-1:1] in ("''", '""') else v.replace("\n","").strip()

    @classmethod
    def arrayRec(cls, lines: str, start: int) -> dict:
        i, r = start, {}

        while True:
            if i >= len(lines):
                break 

            data = lines[i].lstrip().split("#")[0]
            
            if (k:=len(lines[i]) - len(lines[i].lstrip())) > (h:= len(lines[start]) - len(lines[start].lstrip())) or not data.strip():
                i += 1
                continue
        
            if k < h: return r
            
            if data[0] == "-":
                fv = data[1:].strip()
                if not isinstance(r, list): r = []
                content = YamlParser.vp(fv)
                if not fv.strip(): content = YamlParser.arrayRec(lines, i + 1)
                r.append(content)
            else:
                fn, fv = data.split(":")[0], ":".join(data.split(":")[1:]).strip()
                if not isinstance(r, dict): r = {}
                content = YamlParser.vp(fv.strip())
                if not fv.strip(): content = YamlParser.arrayRec(lines, i+1)
                r[fn] = content
            i+=1
        return r
    
    @classmethod
    def yml_parser(cls, filename: str) -> dict:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            output = str(YamlParser.arrayRec(lines, 0)).replace("'", '"').replace(" False", " false").replace(" True", " true").replace("\\\\\"", "\\\"")
            with open(f"{filename.split('.')[0]}_1.json", "w", encoding="utf-8") as of:
                of.write(output)

YamlParser.yml_parser("schedule.yml")
