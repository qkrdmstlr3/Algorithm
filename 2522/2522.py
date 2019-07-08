"""
    Author : ParkEunsik
    Date   : 2019/07/08
    url    : https://www.acmicpc.net/problem/2522
"""
N = int(input())
for i in range(1, N*2):
    if i <= N:
        print(' '*(N-i), '*'*i, sep='')
    else:
        print(' '*(i-N), '*'*(2*N-i), sep='')
