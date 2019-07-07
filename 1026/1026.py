"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/1026
"""
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0

a.sort()
b.sort(reverse=True)
for i in range(N):
    sum += a[i] * b[i]
print(sum)
