# find the sum of three number which is equal to 0
def three_sum(nums):
    res = []
    nums.sort()

    length = len(nums)
    for i in range(length-2):
        l, r = i+i, length-1
        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total < 0:
                l += 1
            elif total>0:
                r -= 1
            else:
                res.append(nums[i],nums[l],nums[r]) 
                l += 1
                r -= 1
    return res


