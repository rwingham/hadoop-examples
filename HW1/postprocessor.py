from csv import reader
from operator import itemgetter
from re import sub


def stripper(word):
    word = sub(r"\(\)\''", "", word)
    return word 

with open('nyt_full.csv', "r") as f:
    with open('nyt_stripped.csv', "w") as sink:
        nytreader = reader(f, delimiter=',')
        for row in nytreader:
            newrow = str(row[0][2:-1]) + "," + str(row[1][:-2]) + "\n"
            sink.write(newrow)