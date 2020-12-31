"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/11656
"""

import sys

text = sys.stdin.readline()
zup = []

for i in range(len(text)-1):
    zup.append(text[i:-1])
zup.sort()
for i in range(len(zup)):
    print(zup[i])
