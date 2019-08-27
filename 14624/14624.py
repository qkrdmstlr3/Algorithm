"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/14624
"""

import sys

N = int(sys.stdin.readline())
if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print('*'*N)
    print(' '*(N//2)+'*')
    for i in range(N//2):
        print(' '*(N//2-i-1)+'*'+' '*(i*2+1)+'*')
