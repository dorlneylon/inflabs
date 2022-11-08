import pandas as pd
import yaml

with open("schedule.yml", "r", encoding="utf8") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

df = pd.DataFrame(data)
df.to_csv("output4.csv", encoding="utf-16", sep='\t', index=False)
