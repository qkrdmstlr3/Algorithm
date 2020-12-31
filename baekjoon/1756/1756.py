"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/1756
"""
import sys

D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))
pizza.reverse()
deep = D

if max(oven) < pizza[-1]:  # 맨 첫 반죽이 들어갈 데가 없을 때
    print(0)
    exit()
for i in range(D):
    if max(oven) < pizza[-1]:
        print(deep)
        exit()
    mi = min(oven)  # 피자를 넣다 막히는 첫 부분
    if mi < pizza[-1]:
        index = oven.index(mi)
        oven = oven[:index]
        deep = index+1
    pizza.pop()
    oven.pop()
    deep -= 1
    if len(pizza) == 0:
        print(deep)
        exit()
print(deep)
