"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/2805
    correct percentage : 29.018%
"""
import sys

N, cnt = int(sys.stdin.readline()), 0

while N >= 0:
    if N % 5 == 0:
        break
    else:  # 작은 것을 빼면서 5로 나눠질 때까지 기다림
        N -= 3
        cnt += 1
if N < 0:  # 5로 안 나눠지고 음수 나오면 -1 출력
    print(-1)
else:
    while N != 0:  # 5로 나눠지면 실행
        cnt += 1
        N -= 5
    print(cnt)
