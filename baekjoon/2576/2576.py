"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2576
"""

import sys

odd = []
for i in range(7):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        odd.append(num)
if not len(odd):
    print(-1)
else:
    print(sum(odd), min(odd), sep='\n')
