#!/usr/bin/env python

from sys import stdin, stdout
from collections import defaultdict

#from assignment
def output(key, value):
    print(key + '\t' + str(value))
    

if __name__ == '__main__':
    for l in stdin: 
        line = l.split(" ")
        #short version
        if 1:
            for word in line:
                output(word, 1)
             #long version
        if 0:
            counts_dict = defaultdict(int)
            for word in line:
                counts_dict[word] += 1
            for key, value in counts_dict.items():
                output(key,value)
