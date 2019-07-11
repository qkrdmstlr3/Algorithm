"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/2583
"""
num1 = int(input())
num2 = int(input())


print(num1*(num2 % 10))
print(num1*int(((num2 % 100)/10)))
print(num1*int(num2/100))
print(num1*num2)
