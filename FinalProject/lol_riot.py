from pyspark import SparkContext
from json import loads
from operator import add
from sys import argv

sc = SparkContext(appName = "RiotDataCounts")

#first argument should be a champ csv, second argument should be an item csv

champ_csv = sc.textFile(argv[1])
item_csv = sc.textFile(argv[2])

champ_counts = champ_csv.map(lambda x: (x, 1))\
                        .reduceByKey(add)

item_counts = item_csv.flatMap(lambda x: (x.split(",")))\
                      .map(lambda x: (x, 1))\
                      .reduceByKey(add)

champout_name = argv[1] + ".txt"
itemout_name = argv[2] + ".txt"

with open(champout_name, "w") as sink:
    for champ, count in champ_counts.collect():
        sink.write("{}\t{}\n".format(champ, count))

with open(itemout_name, "w") as sink:
    for item, count in item_counts.collect():
        sink.write("{}\t{}\n".format(item, count))
