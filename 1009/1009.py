"""
    Author : ParkEunsik
    Date   : 2019/07/06
    url    : https://www.acmicpc.net/problem/1009
"""

T = int(input())
for i in range(T):
    a, b = list(map(int, input().split()))
    a %= 10
    if b == 0:
        print(1)
    elif a == 0:
        print(10)
    else:
        temp = a
        li = []
        while True:
            if a in li:
                break
            else:
                li.append(a)
            a = (a * temp) % 10
        print(li[b % len(li) - 1])
