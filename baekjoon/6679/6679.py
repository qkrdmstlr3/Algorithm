"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/6679
"""


def n_sum(n, jin):
    s = 0
    while n:
        s += n % jin
        n //= jin
    return s


for i in range(2992, 9999):
    a, b, c = n_sum(i, 10), n_sum(i, 12), n_sum(i, 16)
    if a == b and b == c:
        print(i)
