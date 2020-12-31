"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/10989
    solution : 10001배열 선언해서 들어오는 값마다 그 인덱스를 1씩 늘림 max 설정해서 쓸데없이 10001번 도는 것 방지
    주석 달고 돌리면 시간 초과 뜸;;; 파이썬은 정렬에 비효율적;;
    correct percentage : 23.098%
"""

import sys

result = [0]*10001
max = 0
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    result[num] += 1
    if num > max:
        max = num
for i in range(max+1):
    for j in range(result[i]):
        print(i)
