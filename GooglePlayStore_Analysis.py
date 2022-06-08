# GooglePlayStore_Analysis.py

import pandas as pd

path = "D:\ZongZhengFiles\Program\Python_program\DataBase_.csv\googleplaystore.csv"

def main():

    csv_file = pd.read_csv(path)        # frame 2d
    # print(csv_file)
    # print(f"count all : {csv_file.shape}")
    # print(f"column all : {csv_file.columns}")

    """
    Find .csv data wrong --> fix it
    """
    # print("average of top100 app rating : ", csv_file["Rating"].nlargest(100).mean())
    # bug_condition = csv_file[csv_file["Rating"] > 5]
    # print(bug_condition)

    # csv_file = csv_file[csv_file["Rating"] <= 5]
    # print("average of top100 app rating : ", csv_file["Rating"].nlargest(100).mean())

    # print(csv_file[pd.to_numeric(csv_file["Install"])])
    # print(csv_file[pd.to_numeric(csv_file["Install"].str.replace("[],+", ""))])
    # csv_file = pd.to_numeric(csv_file["Install"].str.replace("[],+", "").replace("Free", ""))

    return 0;

main()