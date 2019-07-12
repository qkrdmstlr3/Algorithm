"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/1065
"""
N, cnt = int(input()), 0
for i in range(1, N+1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        a = int(i / 100)
        b = int(i / 10) % 10
        c = i % 10
        if a-b == b-c:
            cnt += 1
print(cnt)
