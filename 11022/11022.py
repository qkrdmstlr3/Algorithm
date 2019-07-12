"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/11022
"""
cnt = int(input())
for i in range(1, cnt+1):
    num = list(map(int, input().split()))
    print("Case #", i, ": ", num[0], " + ", num[1], " = ", num[0]+num[1], sep='')
