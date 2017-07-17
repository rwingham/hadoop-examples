from pyspark import SparkContext
from json import loads
from datetime import datetime
from operator import add
from nltk.tokenize import casual
from nltk.corpus import stopwords
from collections import defaultdict
from math import log
from re import match, compile

#City-week pairs used (from spreadsheet analysis)
#Portland - 43
#nyc - 5
#Seattle - 32

CITY = 'Seattle'
WEEK = 32

sc = SparkContext(appName = "NYCFreqCounts")

reddit_all = sc.textFile('hdfs:/data/reddit/')

def get_week(comment):
    week = datetime.fromtimestamp(float(comment['created_utc'])).isocalendar()[1]
    return week

c = 0 #words in busy week
d = 0 #words in all other weeks

def get_words(comments):
    tokenizer = casual.TweetTokenizer()
    sc.broadcast(tokenizer)
    stops = stopwords.words('english')
    sc.broadcast(stops)
    alpha_re = compile('^[a-zA-Z]+$')
    sc.broadcast(alpha_re)
    comment = comments.map(lambda x: x['body'])
    words = comment.flatMap(lambda y: tokenizer.tokenize(y))\
                   .map(lambda b: b.lower())\
                    .filter(lambda z: z not in stops)\
                    .filter(lambda a: alpha_re.match(a))
    return(words)

#actually all comments except the week in question
comments_all = reddit_all.map(lambda line:loads(line))\
                         .filter(lambda x: x['subreddit'] == CITY)\
                         .filter(lambda y: get_week(y) != WEEK)
                                 
words_all = get_words(comments_all).map(lambda x: (x, 1))\
                                   .reduceByKey(add)

full_words = defaultdict(lambda: 1)
for word, frequency in words_all.collect():
    full_words[word] = frequency
    d += frequency

comments_busy = reddit_all.map(lambda line: loads(line))\
                       .filter(lambda x: x['subreddit'] == CITY)\
                       .filter(lambda y: get_week(y) == WEEK)

words_busy = get_words(comments_busy).map(lambda x: (x, 1))\
                     .reduceByKey(add)

for word, frequency in words_busy.collect():
    c += frequency

#a: x[1]
#b: full_words[x[0]]
#c: c
#d: d

log_likelihood = words_busy.map(lambda x:(x[0], (2 * (x[1] * (log (x[1]) -  log(c * (x[1] + full_words[x[0]])) - log(c + d)))\
                                                 + full_words[x[0]] * (log (full_words[x[0]]) - log (d) + log(x[1] + full_words[x[0]]))\
                                                                       - log (c + d))))

with open("sea_frequency.txt", "w") as sink:
    for word, ll in log_likelihood.collect():
        sink.write("{}\t{}\n".format(word, ll))
