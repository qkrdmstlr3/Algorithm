"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/1110
"""
N, cnt = int(input()), 0
M = N
while True:
    N = (N % 10)*10 + (N % 10+int(N/10)) % 10
    cnt += 1
    if M == N:
        break
print(cnt)
