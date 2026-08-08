class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for index, value in enumerate(nums):
            num_to_find = target - value
            if num_to_find in store:
                return [store[num_to_find], index]
            else:
                store[value] = index