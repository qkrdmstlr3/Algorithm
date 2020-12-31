"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/9455
"""

import sys

for i in range(int(sys.stdin.readline())):
    m, n = map(int, sys.stdin.readline().split())
    li, cnt = [], 0
    for j in range(m):
        li.append(list(sys.stdin.readline().split()))
    for j in range(n):
        cnt2 = 0  # 아래에 있는 박스를 카운트
        for k in reversed(range(m)):
            if li[k][j] == '1':
                cnt2 += 1
                cnt += m-k-cnt2
    print(cnt)
