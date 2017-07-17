#!/usr/bin/env python

from sys import stdin

ABBREV = "St" #the abbreviation we're extracting; change it here!

#extract context for lines we care about
def chop_line(line):
    
    for i in range(len(line)):
        if line[i] == ABBREV:
            line = line[i-4:i+5]
            return line
    pass

def classify_token(word):
    token = word[0]
    if word == ABBREV: #the one we're looking for 
        return "_"
    try:
        int(token)
        return "N"
    except:
        pass
    if token == "-":
        return "-"
    if not token.isalpha():
        return "P"
    if token.isupper():
        return "U"
    if token.islower():
        return "L"
    pass

#from assignment
def output(key, value):
    print(key + '\t' + " ".join(value))
    
if __name__ == '__main__':
    padder = ["-", "-", "-"]
    for line in stdin:
        line = line.split(" ")
        line = padder + line + padder
        context = chop_line(line)
        if context is not None:
            outstr = ""
            for word in context:
                outstr = outstr + str(classify_token(word))
            if len(outstr) > 0: #don't output if the word wasn't in there
                output(outstr, context)  
