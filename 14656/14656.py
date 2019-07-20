"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/14656
"""
import sys

N = int(sys.stdin.readline())
num, s = list(map(int, sys.stdin.readline().split())), 0
for i in range(N):
    if i + 1 != num[i]:
        s += 1
print(s)
