"""
    Author : ParkEunsik
    Date   : 2019/07/08
    url    : https://www.acmicpc.net/problem/10995
"""
N = int(input())
for i in range(N):
    if i % 2 != 0:
        print(" *"*N)
    else:
        print("* "*N)
