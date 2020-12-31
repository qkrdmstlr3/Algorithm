"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/4673
"""


def sum_digit(numb):
    a = 0
    while int(numb/1) != 0:
        a += numb % 10
        numb = int(numb/10)
    return a


num = [True]*10001
for i in range(1, 10001):
    if sum_digit(i)+i < 10001:
        num[sum_digit(i)+i] = False
for i in range(1, 10001):
    if num[i] is True:
        print(i)
