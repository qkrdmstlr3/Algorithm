"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2711
"""

import sys

for i in range(int(sys.stdin.readline())):
    N, M = sys.stdin.readline().split()
    print(M[:int(N)-1]+M[int(N):])
