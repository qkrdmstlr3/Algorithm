"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2292
"""

N, cnt, num = int(input()), 1, 1
if N == 1:
    print(1)
else:
    while num < N:
        num += 6*cnt
        cnt += 1
    print(cnt)
