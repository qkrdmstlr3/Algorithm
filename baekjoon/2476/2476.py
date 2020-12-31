"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/2476
    최빈값 사용
"""

import sys
from collections import Counter

price = []
for i in range(int(sys.stdin.readline())):
    dice = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(dice)
    mode = cnt.most_common(1)
    if mode[0][1] == 1:
        price.append(max(dice)*100)
    elif mode[0][1] == 2:
        price.append(1000+mode[0][0]*100)
    else:
        price.append(10000+mode[0][0]*1000)
print(max(price))
