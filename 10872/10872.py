"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10872
"""


def pactorial(N):
    num = 1
    for i in range(2, N+1):
        num *= i
    return num


N = int(input())
print(pactorial(N))
