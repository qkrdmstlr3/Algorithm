"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1018
    브루트포스
"""

import sys

row, column = map(int, sys.stdin.readline().split())
chess, mi = [], 2501
for i in range(row):
    chess.append(sys.stdin.readline())
for i in range(row-7):
    for j in range(column-7):
        cnt1, cnt2 = 0, 0
        for n in range(i, i+8):  # 시작이 흰색일 때
            if n % 2 == 0:  # 행이 짝수일 때
                for m in range(j, j+8):
                    if m % 2 == 0 and chess[n][m] != 'W':  # 열이 짝수일 때
                        cnt1 += 1
                    elif m % 2 == 1 and chess[n][m] != 'B':  # 열이 홀수일 때
                        cnt1 += 1
            else:  # 행이 홀수일 때
                for m in range(j, j+8):
                    if m % 2 == 0 and chess[n][m] != 'B':  # 열이 짝수일 때
                        cnt1 += 1
                    elif m % 2 == 1 and chess[n][m] != 'W':  # 열이 홀수일 때
                        cnt1 += 1
        for n in range(i, i+8):  # 시작이 검은색일 때
            if n % 2 == 0:
                for m in range(j, j+8):
                    if m % 2 == 0 and chess[n][m] != 'B':
                        cnt2 += 1
                    elif m % 2 == 1 and chess[n][m] != 'W':
                        cnt2 += 1
            else:
                for m in range(j, j+8):
                    if m % 2 == 0 and chess[n][m] != 'W':
                        cnt2 += 1
                    elif m % 2 == 1 and chess[n][m] != 'B':
                        cnt2 += 1
        if mi > min(cnt1, cnt2):
            mi = min(cnt1, cnt2)
print(mi)
