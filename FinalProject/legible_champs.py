from json import load
from sys import argv

champ_names = "./champion.json"
champ_txt = argv[1]
outfile = argv[1] + "legible.txt"

with open(champ_txt, "r") as source:
    with open(outfile, "w") as sink:
        with open(champ_names) as names:
            champlookup = load(names)['data']
            for line in source:
                try:
                    champ, number = line.split("\t")
                    champ_name = champlookup[champ]['name']
                    sink.write("{}\t{}\n".format(champ_name, number))
                except KeyError: #catches the header
                    pass
