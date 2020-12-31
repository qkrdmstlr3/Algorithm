"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2443
"""
N = int(input())
count = N*2-1
for i in range(N):
    print(' '*i, '*'*count, sep='')
    count -= 2
