import pandas as pd
import os
def getData():
    files = os.listdir("dataset/")
    print(files)
    topics = {}
    i = 1
    weeks = []
    for file in files:
        df = pd.read_csv("dataset/"+file)
        weeks.append("Semana "+str(i))
        i += 1
        for index, row in df.iterrows(): 
            if row["topic"] in topics.keys():
                topics[row["topic"]].append(row["probability"])
            else:
                topics[row["topic"]] = [row["probability"]]
    return topics, weeks
#print(topics)
