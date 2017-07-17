from json import load
from sys import argv

item_names = "./item.json"
item_txt = argv[1]
outfile = argv[1] + "legible.txt"

with open(item_txt, "r") as source:
    with open(outfile, "w") as sink:
        with open(item_names) as names:
            itemlookup = load(names)['data']
            for line in source:
                try:
                    item, number = line.split("\t")
                    item_name = itemlookup[item]['name']
                    sink.write("{}\t{}\n".format(item_name, number))
                except KeyError: #catches the header
                    pass
