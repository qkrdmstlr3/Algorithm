"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1436
    브루트포스
"""

N, cnt, i = int(input()), 1, 666
while True:
    if cnt == N:
        print(i)
        break
    i += 1
    if '666' in str(i):
        cnt += 1
