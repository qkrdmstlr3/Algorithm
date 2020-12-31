"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/1003
    correct_percentage : 29.141%
    그냥 매번 순환하면 비효율적, 이전것을 기억해 놓는것이 더 편하다
"""
import sys

zero, one = 0, 0
fibonacci_zero = [0]*41
fibonacci_one = [0]*41

fibonacci_zero[0], fibonacci_one[1] = 1, 1  # 0과 1일때를 설정해줌
for i in range(2, 41):
    fibonacci_zero[i] = fibonacci_zero[i-1] + fibonacci_zero[i-2]
    fibonacci_one[i] = fibonacci_one[i-1] + fibonacci_one[i-2]

for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    print(fibonacci_zero[N], fibonacci_one[N])
