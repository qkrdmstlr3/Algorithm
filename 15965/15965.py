"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/16170
    진또배기 에라스토테네스의 체
"""

import sys
import math

K = int(sys.stdin.readline())

li = [True]*(10000000+1)
li[0], li[1] = False, False
for i in range(2, int(math.sqrt(10000000))+1):
    if li[i] is True:
        for j in range(i*i, 10000000, i):  # 효율적으로 범위 지정
            li[j] = False
count = 0
for i in range(2, len(li)):
    if li[i] is True:
        count += 1
        if count == K:
            print(i)
            break
