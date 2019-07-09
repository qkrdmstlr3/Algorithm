"""
    Author : ParkEunsik
    Date   : 2019/07/09
    url    : https://www.acmicpc.net/problem/10991
"""
N = int(input())

print(' '*(N-1), '*', sep='')
if N != 1:
    for i in range(1, N-1):
        print(' '*(N-i-1), '*', ' '*(i*2-1), '*', sep='')
    print('*'*(2*N-1))
