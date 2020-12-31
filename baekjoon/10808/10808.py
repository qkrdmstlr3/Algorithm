"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/10808
"""

import sys

alpha = [0]*26
text = sys.stdin.readline()

for i in range(len(text)-1):
    alpha[ord(text[i])-97] += 1
for i in range(26):
    print(alpha[i], end=' ')

