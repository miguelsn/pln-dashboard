import pandas as pd
def getData():
    files = ["dataset/week1.csv" ,"dataset/week2.csv","dataset/week3.csv"]
    topics = {}

    for file in files:
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            if row["topic"] in topics.keys():
                topics[row["topic"]].append(row["probability"])
            else:
                topics[row["topic"]] = [row["probability"]]
    return topics
#print(topics)
