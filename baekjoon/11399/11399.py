"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/11399
"""

N, s = int(input()), 0
li = list(map(int, input().split()))
li.sort()
for i in range(len(li)):
    s += li[i]*(N-i)
print(s)
