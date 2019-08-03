"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/12791
"""
import sys

db = [[1967, 'DavidBowie'], [1969, 'SpaceOddity'], [1970, 'TheManWhoSoldTheWorld'], [1971, 'HunkyDory'], [1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'], [1973, 'AladdinSane'], [1973, 'PinUps'], [1974, 'DiamondDogs'], [1975, 'YoungAmericans'], [1976, 'StationToStation'], [1977, 'Low'], [1977, 'Heroes'], [1979, 'Lodger'], [1980, 'ScaryMonstersAndSuperCreeps'], [1983, 'LetsDance'], [1984, 'Tonight'], [1987, 'NeverLetMeDown'], [1993, 'BlackTieWhiteNoise'], [1995, '1.Outside'], [1997, 'Earthling'], [1999, 'Hours'], [2002, 'Heathen'], [2003, 'Reality'], [2013, 'TheNextDay'], [2016, 'BlackStar']]


for i in range(int(sys.stdin.readline())):
    count, result = 0, []
    s, e = map(int, sys.stdin.readline().split())
    for j in range(25):
        if db[j][0] > e:
            break
        elif db[j][0] >= s:
            count += 1
            result.append(db[j])
    print(count)
    for j in range(len(result)):
        print(result[j][0], result[j][1])
