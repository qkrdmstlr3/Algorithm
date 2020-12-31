"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/5612
"""
import sys

n, T = map(int, sys.stdin.readline().split())
work, cnt = list(map(int, sys.stdin.readline().split())), 0

for i in range(n):
    if sum(work[:i+1]) > T:
        break
    else:
        cnt += 1
print(cnt)
