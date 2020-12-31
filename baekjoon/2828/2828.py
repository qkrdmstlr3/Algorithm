"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/2828
"""
import sys

n, m = map(int, sys.stdin.readline().split())
basket_start, basket_end = 1, m
distance = 0
for i in range(int(sys.stdin.readline())):
    apple = int(sys.stdin.readline())
    if apple >= basket_start and apple <= basket_end:
        continue
    elif apple < basket_start:
        distance += basket_start - apple
        basket_end -= (basket_start-apple)
        basket_start = apple
    elif apple > basket_end:
        distance += apple - basket_end
        basket_start += (apple - basket_end)
        basket_end = apple
print(distance)
