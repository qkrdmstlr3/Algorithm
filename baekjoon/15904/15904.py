"""
    Author : ParkEunsik
    Date   : 2019/09/19
    url    : https://www.acmicpc.net/problem/15904
"""

import sys

text = list(sys.stdin.readline().rstrip())
ucpc = ['U', 'C', 'P', 'C']
flag = True

for i in range(4):
    if ucpc[i] not in text:
        flag = False
        break
    text = text[text.index(ucpc[i]):]
print("I love UCPC") if flag else print("I hate UCPC")
