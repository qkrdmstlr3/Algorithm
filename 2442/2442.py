"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2442
"""
N = int(input())
count = 1
for i in range(N):  # count = i*2+1
    print(' '*(N-i-1), '*'*count, sep='')
    count += 2
