"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2444
"""
N = int(input())
count = N*2-1
for i in range(N):
    print(' '*i, '*'*count, sep='')
    count -= 2
count += 4
for i in range(N-1):
    print(' '*(N-2-i), '*'*count, sep='')
    count += 2
