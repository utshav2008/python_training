def two_sum(nums, target):
    sum_dict = {}
    for i in range(len(nums)):
        if nums[i] in sum_dict:
            return(sum_dict[nums[i]], i)
        else:
            sum_dict[target - nums[i]] = i

print(two_sum([2,7,11,19],9))