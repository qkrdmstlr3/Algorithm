"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/14593
    correct percentage : 41.834%
    항상 g팀이 이긴다는 것을 고려;;
"""

import sys

jeminis = list(map(int, sys.stdin.readline().split()))
girlibus = list(map(int, sys.stdin.readline().split()))
j_count = 0
g_count = 0
flag = False
for i in range(9):
    j_count += jeminis[i]
    if j_count > g_count:
        flag = True
    g_count += girlibus[i]
print("Yes") if flag else print("No")
