"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1181
    correct percentage : 37.556%
"""

import sys
from operator import itemgetter

text = [[] for _ in range(51)]
for i in range(int(sys.stdin.readline())):
    word = sys.stdin.readline()
    if word not in text[len(word)-1]:
        text[len(word)-1].append(word)
for i in range(len(text)):
    if not len(text[i]) == 0:
        text[i].sort()
        print(''.join(text[i]), end='')
