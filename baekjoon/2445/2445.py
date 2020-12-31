"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2444
"""
N = int(input())
for i in range(N):
    print('*'*(i+1), ' '*(2*(N-i-1)), '*'*(i+1), sep='')
for i in range(N-1):
    print('*'*(N-1-i), ' '*(2*(i+1)), '*'*(N-1-i), sep='')
