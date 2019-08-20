"""
    Author : ParkEunsik
    Date   : 2019/08/20
    url    : https://www.acmicpc.net/problem/2587
"""

import sys

li = []
for i in range(5):
    li.append(int(sys.stdin.readline()))
li.sort()
print(sum(li)//5)
print(li[2])
