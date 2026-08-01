class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        array_length = n*2
        ans = [0]*array_length

        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans