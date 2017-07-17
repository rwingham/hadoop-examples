from pyspark import SparkContext
from json import loads
from datetime import datetime
from operator import add

sc = SparkContext(appName = "Reddit raw by-week")

reddit_all = sc.textFile('hdfs:/data/reddit/').cache()

def get_week(comment):
    week = datetime.fromtimestamp(float(comment['created_utc'])).isocalendar()[1]
    return week

comments = reddit_all.map(lambda line: loads(line))\
                          .map(lambda y: (get_week(y), 1))\
                          .reduceByKey(add)
output = comments.sortByKey(ascending = True)

with open("reddit_byweek.txt", "w") as sink:
    for timestamp, n_comments in output.collect():
        sink.write("{}\t{}\n".format(timestamp, n_comments))
