"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/1427
"""

import sys

li = list(sys.stdin.readline())
li.sort(reverse=True)  # 문자도 sort 됨;;

for i in range(len(li)):
    print(li[i], end='')
