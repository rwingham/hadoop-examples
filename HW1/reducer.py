#!/usr/bin/env python

from collections import defaultdict
from sys import stdin

if __name__ == "__main__":
    count_dict = defaultdict(int)
    for l in stdin:
        line = l.split('\t')
        try:
            key = line[0]
            value = int(line[1])
            count_dict[key] += value
        except: #just ignore empty lines
            pass
    for key, value in count_dict.items():
        print(key, value)
