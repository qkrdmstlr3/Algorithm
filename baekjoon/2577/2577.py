"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/2577
"""

result = str(int(input())*int(input())*int(input()))
num = [0]*10
for i in range(len(result)):
    num[int(result[i])] += 1
for i in range(10):
    print(num[i])
