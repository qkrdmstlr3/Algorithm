"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1592
"""

import sys

N, M, L = map(int, sys.stdin.readline().split())

person = [0]*(N)
person[0] = 1
index = 0
count = 0
while True:
    if person[index] % 2 != 0:
        index = (index+L) % N
    else:
        index = (index-L) % N
    person[index] += 1
    count += 1
    if person[index] == M:
        break
print(count)
