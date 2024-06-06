def subarray_sum_equals_k(self, nums: List[int], k: int) -> int:
        # write your code here
        sum_dict = {0:1}
        count = 0
        sum = 0

        for num in nums:
            sum += num
            if (sum-k) in sum_dict:
                count += sum_dict[sum-k]
            if sum in sum_dict:
                sum_dict[sum] += 1
            else:
                sum_dict[sum] = 1
        return count
