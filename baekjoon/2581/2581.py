"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/2581
    correct percentage : 38.026%
    에라스토테네스의 체
"""
import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

li = [True]*(N+1)
li[0], li[1], n_sum = False, False, []

for i in range(2, int(math.sqrt(N))+1):  # 제곱근 구하기
    if li[i] is False:  # 이미 지워진 수는 내버려둔다
        continue
    for j in range(2, N//2+1):
        if i*j > N:
            break
        li[i*j] = False
for i in range(M, N+1):
    if li[i] is True:
        n_sum.append(i)
if not len(n_sum):
    print(-1)
else:
    print(sum(n_sum))
    print(n_sum[0])
