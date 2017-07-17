#!/usr/bin/env python

from collections import defaultdict
from sys import stdin

N_MAX = 100 #max examples each

if __name__ == '__main__':
    counts_dict = defaultdict(int)
    output_dict = {}
    for line in stdin:
        line = line.split('\t')
        if len(line) == 2: #handle weird empty lines without crashing
            key = line[0]
            value = line[1]
            counts_dict[key] += 1
            if counts_dict[key] < N_MAX: #only 100 per type
                if value not in (list(output_dict.values())): #no duplicates
                    output_dict[key] = value
    for k,v in output_dict.items():
        print(k, v)
