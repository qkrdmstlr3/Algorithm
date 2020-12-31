"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/11720
"""
N, num, n_sum = input(), input(), 0
for i in range(len(num)):
    n_sum += int(num[i])
print(n_sum)
