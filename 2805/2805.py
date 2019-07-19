"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/2805
    correct percentage : 25.534%
    시간 초과 나서 pypy3로 제출
"""
# tall의 값을 반으로 나누면서 품
import sys


def n_sum(h, t):  # 가져갈 수 있는 나무 높이의 총합을 계산
    s = 0
    for i in range(len(h)):
        if h[i] > t:
            s += h[i] - t
    return s


N, M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
mx_h, mi_h = max(height), 0
tall = (mx_h + mi_h) // 2

while True:
    h_s = n_sum(height, tall)
    if h_s < M:  # M보다 작아서 기준치를 낮춤
        mx_h = tall
        tall = (mx_h + mi_h) // 2
    elif h_s > M:
        if n_sum(height, tall+1) < M:  # 더 높게 자를수 있는 값이 있을 수도 있어서 검사해줌
            break  # 없으면 통과
        else:
            mi_h = tall
            tall = (mx_h + mi_h) // 2
    else:  # 같으면 그냥 통과
        break
print(tall)
