# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:40:31 2019

@author: marle
"""
EXERCISE 7.2
fh = open("mbox-short.txt", 'r')
count = 0
tot = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[20:])
    tot = num + tot
average = tot / count
print("Average spam confidence:", average)
