"""
    Author : ParkEunsik
    Date   : 2019/10/03
    url    : https://www.acmicpc.net/problem/3449
"""

import sys

for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print("Hamming distance is ",count,".",sep='')