"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/4458
    correct percentage: 46.678%
"""

import sys

for i in range(int(sys.stdin.readline())):
    sentence = list(sys.stdin.readline().rstrip())
    if ord(sentence[0]) >= 97:
        sentence[0] = chr(ord(sentence[0])-32)
    print(''.join(sentence))
