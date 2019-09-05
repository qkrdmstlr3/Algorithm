"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/12780
"""

import sys

H = sys.stdin.readline().rstrip()
N = sys.stdin.readline().rstrip()
count = 0

for i in range(len(H)-len(N)+1):
    if H[i] == N[0] and N == H[i:i+len(N)]:
        count += 1
print(count)
