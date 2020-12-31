"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1431
"""

import sys
from operator import itemgetter

N = int(sys.stdin.readline())
guitar = []

for _ in range(N):
    serial = sys.stdin.readline().rstrip()
    num = 0
    for i in serial:
        if '0' <= i <= '9':
            num += int(i)
    guitar.append([serial, num])
guitar.sort(key=len)
sn_length = [[] for _ in range(51)]
for i in range(N):  # 시리얼 넘버를 길이별로 나눔
    sn_length[len(guitar[i][0])].append(guitar[i])
for i in range(len(sn_length)):  # 길이별로 2,3번 조건 비교 후 출력
    if sn_length[i] != 0:
        sn_length[i].sort(key=itemgetter(1, 0))
        for j in sn_length[i]:
            print(j[0])
