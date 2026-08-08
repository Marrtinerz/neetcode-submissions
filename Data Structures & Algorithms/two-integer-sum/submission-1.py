class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        store = {}

        for j, num in enumerate(nums):
            num_to_find = target - num
            if num_to_find in store:
                i = store[num_to_find]
                return [i, j]
            else:
                store[num] = j