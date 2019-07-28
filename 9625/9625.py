"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/9625
"""

import sys

cnt_a, cnt_b = 1, 0
for i in range(int(sys.stdin.readline())):
    temp = cnt_b
    cnt_b += cnt_a
    cnt_a = temp
print(cnt_a, cnt_b)
