"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/1978
    에라스토테네스의 체
"""
import sys
import math

N = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))

li = [True]*1001
li[0], li[1], cnt = False, False, 0

for i in range(2, int(math.sqrt(1001))):  # 제곱근 구하기
    if li[i] is False:  # 이미 지워진 수는 내버려둔다
        continue
    for j in range(2, 500):
        if i*j > 1000:
            break
        li[i*j] = False
for i in range(len(num)):
    if li[num[i]] is True:
        cnt += 1
print(cnt)
