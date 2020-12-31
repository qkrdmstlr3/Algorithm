"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/10952
"""
while True:
    num = list(map(int, input().split()))
    A, B = num[0], num[1]
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
