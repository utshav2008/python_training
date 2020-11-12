def subsets(nums):
    sol = []
    helper(nums, sol, [], 0)
    return sol

def helper(nums, sol, curr, index):
    sol.append(list(curr))
    for i in range(index, len(nums)):
        curr.append(nums[i])
        helper(nums, sol, curr, i+1 )
        curr.pop()

#
nums = [1,2,3]
print(subsets(nums=nums))
# cur = []
# for i in range(0,len(nums)):
#     cur.append(nums[i])
#
# print(cur)
# curr = [2,3]
# for i in range(2, len(nums)):
#     curr.append(nums[i])
#     # helper(nums, sol, curr, i + 1)
#     print(curr)
#     # curr.pop()