"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/15552
    소수점 자리 표시 : https://pyformat.info/#number_padding
"""

import sys

for i in range(int(input())):
    case, cnt = list(map(int, sys.stdin.readline().split())), 0
    average = sum(case[1:])/case[0]
    for j in range(1, case[0]+1):
        if case[j] > average:
            cnt += 1
    print('{:0.3f}'.format(cnt/case[0]*100), "%", sep='')
