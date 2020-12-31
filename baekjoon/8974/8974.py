"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/8974
"""
import sys

a, b = map(int, sys.stdin.readline().split())
number = []
for i in range(1, 50):
    for j in range(i):
        number.append(i)
print(sum(number[a-1:b]))
