"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/10996
"""
N = int(input())

for i in range(2*N):
    for j in range(N):
        if (i & 1) == (j & 1):  # 짝수면 0이고 홀수면 1이 됨
            print("*", end='')
        else:
            print(" ", end='')
    print()
