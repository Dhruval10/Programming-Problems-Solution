def sumInRange(nums, qs):
    ans, s = 0, [nums[0]]
    for i in range(1, len(nums)): s.append(s[-1] + nums[i])
    return sum(s[j] - s[i-1]*(i!=0) for i, j in qs) % 1000000007
