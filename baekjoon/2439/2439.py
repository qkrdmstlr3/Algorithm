"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2439
"""
N = int(input())
for i in range(N):
    print(' '*(N-i-1), '*'*(i+1), sep='')  # sep사용 붙여서 출력
