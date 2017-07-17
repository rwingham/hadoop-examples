from pyspark import SparkContext
from json import loads
from datetime import datetime
from operator import add
from re import sub

CITIES = ['nyc', 'Portland', 'seattle', 'Seattle']

sc = SparkContext(appName = "Reddit raw by-week")

reddit_all = sc.textFile('hdfs:/data/reddit/')

def get_week(comment):
    week = datetime.fromtimestamp(float(comment['created_utc'])).isocalendar()[1]
    return week

comments = reddit_all.map(lambda line: loads(line))\
                     .filter(lambda x: x['subreddit'] in CITIES)\
                     .map(lambda y: (y['subreddit'] + "-" + str(get_week(y)), 1))\
                     .reduceByKey(add)
output = comments.sortByKey(ascending = True)

with open("subreddit_byweek.txt", "w") as sink:
    for timestamp, n_comments in output.collect():
        timestamp = sub('-','\t', timestamp)
        sink.write("{}\t{}\n".format(timestamp, n_comments))
