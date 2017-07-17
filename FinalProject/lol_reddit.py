from pyspark import SparkContext
from json import loads
from nltk.tokenize import casual
from nltk.corpus import stopwords
from operator import add

from collapse2canonical import champ_list, item_list, collapse_champ, collapse_item

SUBREDDITS = ['leagueoflegends', 'leagueoflegendsmeta', 'summonerschool']

sc = SparkContext(appName = "LolRedditData", pyFiles=['collapse2canonical.py'])

reddit_all = sc.textFile('hdfs:/data/reddit')

champs = champ_list()
items = item_list()

def get_words(comments):
    tokenizer = casual.TweetTokenizer()
    sc.broadcast(tokenizer)
    stops = set(stopwords.words('english'))
    sc.broadcast(stops)
    unique_id = comments.map(lambda x: x['id'])
    words = comments.flatMap(lambda y: tokenizer.tokenize(y['body']))\
                    .map(lambda b: b.lower())\
                    .filter(lambda z: z not in stops)
    return(words)

comments = reddit_all.map(lambda line: loads(line))\
                          .filter(lambda x: x['subreddit'].lower() in SUBREDDITS)

words_by_id = get_words(comments)
champ_counter = words_by_id.filter(lambda b: b in champs)\
                           .map(lambda a: collapse_champ(a))\
                           .map(lambda d: (d, 1))\
                           .reduceByKey(add)
item_counter = words_by_id.filter(lambda b: b in items)\
                          .map(lambda a: collapse_item(a))\
                          .map(lambda d: (d, 1))\
                          .reduceByKey(add)

with open("champ_counts.txt", "w") as sink:
    for champ, count in champ_counter.collect():
        sink.write("{}\t{}\n".format(champ, count))

with open("item_counts.txt", "w") as sink:
    for item, count in item_counter.collect():
        sink.write("{}\t{}\n".format(item, count))



#emit ID, use to combine down the line
#get list of items and champs, then map that into something
