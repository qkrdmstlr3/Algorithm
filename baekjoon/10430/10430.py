"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10430
"""
num = list(map(int, input().split()))
print((num[0]+num[1]) % num[2])
print((num[0] % num[2]+num[1] % num[2]) % num[2])
print(num[0]*num[1] % num[2])
print((num[0] % num[2] * num[1] % num[2]) % num[2])
