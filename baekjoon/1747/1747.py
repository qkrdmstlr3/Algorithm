"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1735
    correct percentage : 23.954%
    에라스토테네스의 체로 거른 후 숫자를 1씩 키워가며 맞는지 체크
"""

import sys
import math

N = int(input())
li = [True]*(1004000+1)
li[0], li[1] = False, False
for i in range(2, int(math.sqrt(1004000))+1):
    if li[i] is False:
        continue
    for j in range(2, 502000):
        if i*j > 1004000:
            break
        li[i*j] = False
while True:
    check = list(str(N))
    if li[N] == False:  # 소수인지를 먼저 체크해줌
        N += 1
        continue
    flag = True
    for i in range(len(check)//2):
        if check[i] != check[-i-1]:
            flag = False
    if flag:
        print(N)
        break
    else:
        N += 1
