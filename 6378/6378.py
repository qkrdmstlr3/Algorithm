"""
    Author : ParkEunsik
    Date   : 2019/10/03
    url    : https://www.acmicpc.net/problem/6378
    correct percentage : 40.904%
"""

import sys

while True:
    num = list(sys.stdin.readline().rstrip())
    if num[0] == '0':
        break
    while len(num) > 1:
        num = map(int, num)
        num = list(str(sum(num)))
    print(int(num[0]))