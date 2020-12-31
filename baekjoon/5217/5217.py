"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5217
"""

import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    result = []
    for i in range(1, n//2+1):
        num1 = i
        num2 = n-i
        if i != (n-i):
            result.append((num1, num2))
    print("Pairs for ", n, ": ", sep='', end='')
    for i in range(len(result)):
        print(result[i][0], result[i][1], end='')
        if i != len(result)-1:
            print(', ', end='')
    print()
        
