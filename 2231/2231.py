"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2231
    브루트포스
"""


def sum_digit(number):
    s = number
    while number//1 != 0:
        s += number % 10
        number //= 10
    return s


N = int(input())
for i in range(0, N+1):
    if i == N:
        print(0)
        break
    if sum_digit(i) == N:
        print(i)
        break
