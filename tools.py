'''
Author: Alchemist
Date: 2023-08-11
LastEditTime: 2023-08-11
FilePath: /RabiBear-Home-Web/tools.py
Description: 

Copyright (c) 2023, All Rights Reserved. 
'''
import csv
import json

def trans_csv_to_dict(path):
    rows = []
    with open(path, encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
            rows.append(row[0])
    out = []
    for idx, item in enumerate(rows):
        out.append({'isdone': False, 'content': item})
    json.dump(out, open("/Users/Alchemist/Downloads/RabiBear-Home-Web/server/100things.json", "w",encoding='utf-8'), ensure_ascii=False)


if __name__ == "__main__":
    trans_csv_to_dict("/Users/Alchemist/Downloads/100things.csv")
    
