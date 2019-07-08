"""
    Author : ParkEunsik
    Date   : 2019/07/08
    url    : https://www.acmicpc.net/problem/10990
"""
N = int(input())
print(' '*(N-1), '*', sep='')
if N != 1:
    for i in range(1, N):
        print(' '*(N-i-1), '*', ' '*(i*2-1), '*', sep='')
