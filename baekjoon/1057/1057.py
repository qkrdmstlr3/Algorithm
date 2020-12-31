"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/1057
"""
num = list(map(int, input().split()))
N, kim, lim = num[:3]  # :3 그냥 써보고 싶었다;;
kim, lim, count = kim - 1, lim - 1, 0

while kim != lim:
    kim = int(kim/2)
    lim = int(lim/2)
    count += 1
print(count)
