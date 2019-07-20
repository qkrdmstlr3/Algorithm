"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/1302
"""

import sys

cnt, li, mx = 1, [], 0
for i in range(int(sys.stdin.readline())):
    li.append(sys.stdin.readline())
li.sort()
temp = li[0]
for i in range(len(li)-1):
    if li[i] == li[i+1]:
        cnt += 1
    else:
        cnt = 1
    if mx < cnt:
        temp = li[i]
        mx = cnt
print(temp)
