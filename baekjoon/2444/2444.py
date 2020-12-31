"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2444
"""
N = int(input())
count = 1
for i in range(N):  # 이 반복문에서는 count = i*2+1 이지만 편하게 보기 위해서 count로 넣음
    print(' '*(N-i-1), '*'*count, sep='')
    count += 2
count -= 4
for i in range(N-1):
    print(' '*(i+1), '*'*count, sep='')
    count -= 2
