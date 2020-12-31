"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5363
"""

import sys

for i in range(int(sys.stdin.readline())):
    sentence = list(sys.stdin.readline().split())
    sentence.append(sentence[0])
    sentence.append(sentence[1])
    print(' '.join(sentence[2:]))
