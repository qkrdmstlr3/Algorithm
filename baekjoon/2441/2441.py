"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2441
"""
N = int(input())
for i in reversed(range(N)):
    print(' '*(N-1-i), '*'*(i+1), sep='')
