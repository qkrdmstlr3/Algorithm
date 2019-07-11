"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/2753
"""
N = int(input())
flag1 = False
flag2 = True
if N % 4 == 0:
    flag1 = True
if N % 100 == 0:
    flag2 = False
if N % 400 == 0:
    flag2 = True
if flag1 is True:
    if flag2 is False:
        print(0)
    else:
        print(1)
else:
    print(0)
