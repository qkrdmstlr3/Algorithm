"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/9020
    correct percentage : 46.240%
    에라스토테네스의 체
    휴가 잘려서 멘탈 나가서 코드 지저분함;;
"""
import sys
import math

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    li = [True]*(num+1)  # 입력받은 수 포함해 하나 더 크게 설정
    li[0], li[1], cnt = False, False, 0
    # 에라스토테네스의 체
    for i in range(2, int(math.sqrt(num))+1):  # 제곱근 구하기
        if li[i] is False:  # 이미 지워진 수는 내버려둔다
            continue
        for j in range(2, num//2):
            if i*j > num:
                break
            li[i*j] = False
    min = 10000  # 최소를 찾기 위함
    a, b = 0, 0
    for i in reversed(range(num//2-1, num)):
        if li[num - i] is True and li[i] is True:
            if min > abs(num-i-i):
                min = abs(num-i-i)
                a, b = num-i, i
            elif min < abs(num-i-i):
                break
    print(a, b)
