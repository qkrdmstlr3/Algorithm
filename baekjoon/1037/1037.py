"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/1037
"""
N = int(input())
num = list(map(int, input().split()))
num.sort()

if len(num) % 2 == 0:
    print(num[0] * num[N-1])
else:
    print(num[int((N-1)/2)]**2)
