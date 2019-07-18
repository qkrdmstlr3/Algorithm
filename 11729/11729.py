"""
    Author : ParkEunsik
    Date   : 2019/07/18
    url    : https://www.acmicpc.net/problem/11729
    기둥 1 > n-1개를 기둥2로(기둥 3 이용)
    기둥 1 > 남은 1개 기둥 3
    기둥 2 > n-1개를 기둥 3로(기둥 1 이용)
"""


def hanoi(n, column1, column2, column3):
    if(n == 1):
        print(column1, column3)
    else:
        hanoi(n-1, column1, column3, column2)
        print(column1, column3)
        hanoi(n-1, column2, column1, column3)


N = int(input())
print(2**N-1)
hanoi(N, 1, 2, 3)
