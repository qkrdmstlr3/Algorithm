"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2592
"""

import sys
from collections import Counter

num = []
for i in range(10):
    num.append(int(sys.stdin.readline()))
cnt = Counter(num)
print(sum(num)//10)
print(cnt.most_common(1)[0][0])
