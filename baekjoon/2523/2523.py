"""
    Author : ParkEunsik
    Date   : 2019/07/08
    url    : https://www.acmicpc.net/problem/2523
"""
N = int(input())
for i in range(1, N*2):
    if i <= N:
        print('*'*i)
    else:
        print('*'*(2*N-i))
