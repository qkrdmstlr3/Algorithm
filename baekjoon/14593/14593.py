"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/14593
"""

import sys
from operator import itemgetter

participants = []
for i in range(int(sys.stdin.readline())):
    participants.append(list(map(int, sys.stdin.readline().split()))+[i+1])
participants.sort(reverse=True)
new_array = []
for i in range(len(participants)):
    if participants[i][0] == participants[0][0]:
        new_array.append(participants[i])
new_array.sort(key=itemgetter(1, 2))  # 인덱스 1, 2 기준으로 정렬
print(new_array[0][3])
