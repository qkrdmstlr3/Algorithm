"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/4948
"""
import sys
import math

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        exit()

    li = [True]*(2*N+1)
    li[0], li[1], cnt = False, False, 0

    for i in range(2, int(math.sqrt(2*N+1))+1):  # 제곱근 구하기
        if li[i] is False:  # 이미 지워진 수는 내버려둔다
            continue
        for j in range(2, N+1):
            if i*j > 2*N:
                break
            li[i*j] = False
    cnt = 0
    for i in range(N+1, 2*N+1):
        if li[i] is True:
            cnt += 1
    print(cnt)
