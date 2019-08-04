"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/3004
"""
import sys

N = int(sys.stdin.readline())
if N % 2 != 0:
    a = N//2
    b = N-a
    print((b+1)*b)
else:
    print((N//2+1)**2)

