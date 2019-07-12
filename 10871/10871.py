"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10871
"""
cnt = list(map(int, input().split()))
num = list(map(int, input().split()))
for i in range(cnt[0]):
    if num[i] < cnt[1]:
        print(num[i], end=' ')
