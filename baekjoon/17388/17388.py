"""
    Author : ParkEunsik
    Date   : 2019/08/15
    url    : https://www.acmicpc.net/problem/17389
"""

import sys

li = list(map(int, sys.stdin.readline().split()))
university = ['Soongsil', 'Korea', 'Hanyang']

if sum(li) >= 100:
    print("OK")
else:
    print(university[li.index(min(li))])
