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
if jeminis.count(0) == 9:
    print("No")
else:
    count = 0
    flag = False
    for i in range(9):
        count += jeminis[i]
        temp2 = count
        count -= girlibus[i]
        if (temp2 > 0 and count <= 0):
            flag = True

    print("Yes") if flag else print("No")
