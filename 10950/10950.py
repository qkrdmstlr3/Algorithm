"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10950
"""
N = int(input())
for i in range(N):
    num = list(map(int, input().split()))
    print(num[0]+num[1])
