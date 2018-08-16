import json
import csv

csvdb = './zasuvky.csv'

header = '// This file is generated by getData.py\n\n\
racks = ["Midgard", "Jotunehim", "Asgard"]\n'

data = {}
tel = {}

with open(csvdb, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if row[1][0:1].lower() == "t":
            tel[row[1][1:].lower()] = {
                "line": row[7],
                "dev": {
                    "telefon": "phone",
                    "zadny neni": "empty",
                    "fax/telefon": "fax",
                    "-": "empty"
                }[row[5]]
            }
        else:
            data[row[1].lower()] = {
                "loc": [["", 0, 0, 0, 1, 1][int(row[2])], (int(row[2])%4)+1, int(row[3])],
                "dev": {
                    "pocitac": "computer",
                    "poctac": "computer",
                    "switch": "switch",
                    "tiskarna": "printer",
                    "-": "empty",
                    "": "empty"
                }[row[5]],
                "old": "?"
            }
            if row[4] != "-":
                data[row[1].lower()]["attrib"] = row[4]

with open('data.js', 'w') as f:
    f.write(header)
    f.write('ether = ' + json.dumps(data) + '\n')
    f.write('tel = ' + json.dumps(tel) + '\n')