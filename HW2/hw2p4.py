from pyspark import SparkContext
from json import loads
from datetime import datetime
from re import sub
from operator import add

sc = SparkContext(appName = "WeekIncreases")

reddit_all = sc.textFile('hdfs:/data/reddit/')

def get_month(comment):
    month = datetime.fromtimestamp(float(comment['created_utc'])).month
    return month

def month_sort(comment, month):
    new = comment.filter(lambda ((a, b), c): a == month)\
                 .map(lambda ((x, y), z): (y, z)) #remove month data
    return new

def calc_diff(month1, month2):
    combo = month1.join(month2)
    combo = combo.map(lambda (a, (b, c)): (a,float(b)/float(c)))\
                 .filter(lambda (x, y): ((y < 0.6) or (y > 1.5))) #thresholds for increase/decrease
    return combo

def write_out(month_name, month_info, sink):
    for subreddit, increase in month_info.collect():
        sink.write("{}\t{}\t{}\n".format(month_name, subreddit, increase))

comments = reddit_all.map(lambda line: loads(line))\
                     .map(lambda y: ((get_month(y), y['subreddit']), 1))\
                     .reduceByKey(add)\
                     .filter(lambda (a, b): b > 250)


#process by-month; probably not the best way to do this
jan = month_sort(comments,1)
feb = month_sort(comments,2)
mar = month_sort(comments,3)
apr = month_sort(comments,4)
may = month_sort(comments,5)
jun = month_sort(comments,6)
#there is no july!
aug = month_sort(comments,8)
sep = month_sort(comments,9)
octo = month_sort(comments,10) #oct means something else
nov = month_sort(comments,11)
dec = month_sort(comments,12)

#compare months
jan_feb = calc_diff(jan, feb)
feb_mar = calc_diff(feb, mar)
mar_apr = calc_diff(mar, apr)
apr_may = calc_diff(apr, may)
may_jun = calc_diff(may, jun)
jun_aug = calc_diff(jun, aug) #there is no july!
aug_sep = calc_diff(aug, sep)
sep_octo = calc_diff(sep, octo)
octo_nov = calc_diff(octo, nov)
nov_dec = calc_diff(nov, dec)

with open("weekincreases.txt", "w") as sink:
    write_out("January-February", jan_feb, sink)
    write_out("February-March", feb_mar, sink)
    write_out("March-April", mar_apr, sink)
    write_out("April-May", apr_may, sink)
    write_out("May-June", may_jun, sink)
    write_out("June-August", jun_aug, sink)
    write_out("August-September", aug_sep, sink)
    write_out("September-October", sep_octo, sink)
    write_out("October-November", octo_nov, sink)
    write_out("November-December", nov_dec, sink)

