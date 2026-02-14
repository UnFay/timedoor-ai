ages = [14, 15,6, 10, 17, 18, 20, 21, 19, 10, 25, 21, 10, 20, 15]
ages.sort()
print(ages)
firstEligible = -1
i = 0
while firstEligible == -1:
    if ages[i] >= 16:
        firstEligible = i
    else:
        i += 1
agesEligible = ages[firstEligible:]
print(agesEligible)