n = int(input())
nums = [1, 5, 10, 20, 100]
constraint = 4
multiplier = 1
count = 0
currAns = 0
while currAns != n:
    if nums[constraint] * multiplier < n:
        multiplier = multiplier + 1
        currAns = nums[constraint] * multiplier
        count = count + multiplier
    elif nums[constraint] * (multiplier + 1) > n:
        constraint = constraint - 1
        multiplier = 0
    print(currAns)
print(count)