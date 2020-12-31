"""
    Author : ParkEunsik
    Date   : 2019/08/02
    url    : https://www.acmicpc.net/problem/12790
"""

import sys

for i in range(int(sys.stdin.readline())):
    power = 0
    hp, mp, attack, shield, p_hp, p_mp, p_attack, p_shield = map(int, sys.stdin.readline().split())
    if hp+p_hp > 0:
        power += hp+p_hp
    else:
        power += 1
    if mp+p_mp > 0:
        power += 5*(mp+p_mp)
    else:
        power += 5

    if attack+p_attack > 0:
        power += 2*(attack+p_attack)
    power += 2*(shield + p_shield)
    print(power)
