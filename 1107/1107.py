"""
    Author : ParkEunsik
    Date   : 2019/07/15
    url    : https://www.acmicpc.net/problem/1107
    correct percentage : 21.939%
"""

import sys

N, M = int(input()), int(input())
if M == 0:  # 리모콘이 잘 될 떄
    print(min(abs(N-100), len(str(N))))
    sys.exit()
elif M == 10:  # 모든 숫자 버튼이 고장날 때
    input()
    print(abs(N-100))
    sys.exit()
li = list(input().split())
mi, mx, cnt = '1000000', '1000000', 0
for i in range(N+1):  # 주어진 수 보다 작은 경우 계산
    n = str(N-i)
    flag = True
    for j in range(len(n)):
        if n[j] in li:
            break
        elif j == len(n)-1:  # N에 가장 가까운 수 찾으면 탈출
            mi = n
            flag = False
    if flag is False:
        break
while True:  # 주어진 수 보다 큰 경우 계산
    n = str(N+cnt)
    flag = True
    for j in range(len(n)):  # N에 가장 가까운 수 찾으면 탈출
        if n[j] in li:
            break
        elif j == len(n)-1:
            mx = n
            flag = False
    if flag is False:
        break
    if cnt > abs(N-int(mi)+len(mi)) and mi != '1000000':
        # 너무 많은 연산 방지하기 위해 mi계산이 안되었거나 cnt가 mi최솟값 보다 클 때
        break
    cnt += 1
print(min(abs(N-100), min(abs(N-int(mi)+len(mi)), abs(int(mx)-N+len(mx)))))
# 100에서 그냥 +-로만 조절하는 것과 반복문 두개 값을 비교
